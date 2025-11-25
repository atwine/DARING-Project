import argparse
import json
from pathlib import Path
from typing import List, Tuple, Optional

import pandas as pd
import random
import numpy as np

try:
    from sdv.metadata import SingleTableMetadata
    from sdv.single_table import GaussianCopulaSynthesizer
    from sdmetrics.reports.single_table import QualityReport
except Exception as e:
    # Minimal fix: surface the real import error and provide current install guidance
    # to avoid misleading users with a specific pinned version that may not exist
    # for their Python platform. This preserves core behavior and only improves
    # debuggability per user workflow rules.
    raise SystemExit(
        f"SDV/SDMetrics import failed: {e}\n"
        "Fix: activate your venv and install compatible packages:\n"
        "  python -m pip install -U sdv sdmetrics\n"
        "If the issue persists, also try: python -m pip install -U rdt copulas"
    ) from e

# Justification: sdmetrics>=0.23 removed/relocated PrivacyReport. Make it optional so the
# script runs on current versions while preserving interface by writing a placeholder.
try:
    from sdmetrics.reports.single_table import PrivacyReport  # type: ignore
    _HAS_PRIVACY_REPORT = True
except Exception:
    _HAS_PRIVACY_REPORT = False


def read_csv_with_fallback(path: Path) -> Tuple[pd.DataFrame, str]:
    encodings = ["utf-8", "utf-8-sig", "cp1252", "latin1"]
    last_err: Optional[Exception] = None
    for enc in encodings:
        try:
            df = pd.read_csv(path, low_memory=False, encoding=enc)
            return df, enc
        except Exception as e:
            last_err = e
            continue
    if last_err is not None:
        raise last_err
    raise RuntimeError("Failed to read CSV with fallback encodings.")


def drop_high_card_text(df: pd.DataFrame, threshold_ratio: float, min_len: int) -> List[str]:
    drops: List[str] = []
    n = len(df)
    for c in df.columns:
        s = df[c]
        if s.dtype == object:
            nunq = s.nunique(dropna=True)
            if n > 0 and (nunq / n) >= threshold_ratio:
                drops.append(c)
                continue
            try:
                avg_len = s.dropna().astype(str).str.len().mean()
                if avg_len is not None and avg_len >= min_len:
                    drops.append(c)
            except Exception:
                pass
    return drops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output_csv", default="synthetic_output.csv")
    ap.add_argument("--quality_json", default="quality_report.json")
    ap.add_argument("--privacy_json", default="privacy_report.json")
    ap.add_argument("--rows", type=int, default=0)
    ap.add_argument("--random_seed", type=int, default=42)
    ap.add_argument("--drop_text_high_card", action="store_true")
    ap.add_argument("--high_card_ratio", type=float, default=0.9)
    ap.add_argument("--avg_text_len", type=int, default=80)
    ap.add_argument("--exclude_columns", nargs="*", default=None)
    # Testing flags: allow fast dry runs by limiting rows/columns and skipping reports.
    ap.add_argument("--limit_rows_real", type=int, default=0)
    ap.add_argument("--limit_columns", type=int, default=0)
    ap.add_argument("--skip_quality", action="store_true")
    args = ap.parse_args()

    # Minimal fix for reproducibility: SDV v1.28 single-table sample() does not accept
    # a random_state parameter (confirmed by TypeError at runtime). Seed RNGs here
    # so sampling remains deterministic without changing synthesizer behavior.
    if args.random_seed is not None:
        random.seed(args.random_seed)
        np.random.seed(args.random_seed)

    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"CSV not found: {input_path}")

    df, enc = read_csv_with_fallback(input_path)
    print(f"Loaded CSV with encoding: {enc}")

    excluded: List[str] = []
    if args.exclude_columns:
        for c in args.exclude_columns:
            if c in df.columns:
                excluded.append(c)
    if args.drop_text_high_card:
        drops = drop_high_card_text(df, args.high_card_ratio, args.avg_text_len)
        excluded.extend([c for c in drops if c not in excluded])

    if excluded:
        keep_cols = [c for c in df.columns if c not in excluded]
        print(f"Excluding {len(excluded)} columns from synthesis; keeping {len(keep_cols)}.")
        df_synth = df[keep_cols].copy()
    else:
        df_synth = df.copy()

    # Minimal control for quick tests: limit rows/columns before fitting to reduce runtime.
    if args.limit_rows_real and args.limit_rows_real > 0:
        df_synth = df_synth.head(args.limit_rows_real).copy()
        print(f"Limiting real data rows to: {len(df_synth)}")
    if args.limit_columns and args.limit_columns > 0:
        # Deterministic selection: keep first N columns in current order.
        df_synth = df_synth[df_synth.columns[:args.limit_columns]].copy()
        print(f"Limiting columns to first: {df_synth.shape[1]}")

    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(df_synth)

    synth = GaussianCopulaSynthesizer(metadata, enforce_min_max_values=True)
    synth.fit(df_synth)

    n = args.rows if args.rows > 0 else len(df_synth)
    # SDV v1.28: BaseSingleTableSynthesizer.sample() has no random_state kwarg.
    # We rely on global seeding above to ensure reproducibility.
    synthetic = synth.sample(num_rows=n)

    Path(args.output_csv).parent.mkdir(parents=True, exist_ok=True)
    synthetic.to_csv(args.output_csv, index=False)

    quality = None
    if not args.skip_quality:
        qrep = QualityReport()
        # sdmetrics>=0.23 expects a metadata dict; convert SDV metadata accordingly.
        qrep.generate(real_data=df_synth, synthetic_data=synthetic, metadata=metadata.to_dict())
        # get_properties() returns a pandas DataFrame; convert to JSON-serializable records.
        _props = qrep.get_properties()
        if isinstance(_props, pd.DataFrame):
            _props = _props.reset_index(drop=True).to_dict(orient="records")
        quality = {"overall_score": qrep.get_score(), "properties": _props}
        Path(args.quality_json).write_text(json.dumps(quality, indent=2), encoding="utf-8")

    # If PrivacyReport exists, use it; otherwise write a minimal placeholder to preserve outputs.
    privacy = None
    if not args.skip_quality:
        if _HAS_PRIVACY_REPORT:
            prep = PrivacyReport()
            # Convert SDV metadata to dict for sdmetrics compatibility.
            prep.generate(real_data=df_synth, synthetic_data=synthetic, metadata=metadata.to_dict())
            privacy = {"overall_score": prep.get_score(), "details": prep.get_details()}
        else:
            privacy = {
                "overall_score": None,
                "details": {
                    "status": "unsupported",
                    "reason": "PrivacyReport not available in this sdmetrics version"
                },
            }
        Path(args.privacy_json).write_text(json.dumps(privacy, indent=2), encoding="utf-8")

    print(f"Synthetic saved: {args.output_csv}")
    if not args.skip_quality and quality is not None:
        if privacy is not None and privacy.get("overall_score") is None:
            print(f"Quality score: {quality['overall_score']:.3f}; Privacy score: n/a")
        elif privacy is not None:
            print(f"Quality score: {quality['overall_score']:.3f}; Privacy score: {privacy['overall_score']:.3f}")
        print(f"Reports: {args.quality_json}, {args.privacy_json}")
    else:
        print("Quality/Privacy reports skipped (fast test mode).")


if __name__ == "__main__":
    main()
