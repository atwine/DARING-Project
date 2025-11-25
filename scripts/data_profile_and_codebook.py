import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Optional import: pdfplumber. If missing, we will handle gracefully.
try:
    import pdfplumber  # type: ignore
except Exception:  # pragma: no cover
    pdfplumber = None  # type: ignore


@dataclass
class ColumnSummary:
    name: str
    dtype: str
    inferred_role: str
    n_unique: int
    pct_unique: float
    n_missing: int
    pct_missing: float
    sample_values: List[str]
    stats: Dict[str, float]


def safe_mkdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def infer_datetime_series(s: pd.Series) -> Tuple[pd.Series, bool]:
    if s.dtype.kind in ("M",):
        return s, True

    if s.dtype == object:
        # Heuristic: only try parse when enough non-null and string-like
        non_null = s.dropna()
        if len(non_null) == 0:
            return s, False
        try:
            parsed = pd.to_datetime(non_null, errors="coerce", infer_datetime_format=True)
            ok_ratio = parsed.notna().mean()
            if ok_ratio > 0.9:
                s2 = s.copy()
                s2.loc[non_null.index] = parsed
                return s2, True
        except Exception:
            pass
    return s, False


def infer_numeric_series(s: pd.Series) -> Tuple[pd.Series, bool]:
    if s.dtype.kind in ("i", "u", "f"):
        return s, True
    if s.dtype == object:
        non_null = s.dropna()
        if len(non_null) == 0:
            return s, False
        coerced = pd.to_numeric(non_null, errors="coerce")
        ok_ratio = coerced.notna().mean()
        if ok_ratio > 0.95:
            s2 = pd.to_numeric(s, errors="coerce")
            return s2, True
    return s, False


def is_boolean_like(s: pd.Series) -> bool:
    # Common boolean encodings: Yes/No, True/False, 0/1
    non_null = s.dropna().astype(str).str.strip().str.lower().unique().tolist()
    non_null = [v for v in non_null if v != ""]
    candidates = [
        {"yes", "no"},
        {"true", "false"},
        {"0", "1"},
    ]
    for c in candidates:
        if set(non_null).issubset(c):
            return True
    return False


def infer_role(name: str, s: pd.Series) -> str:
    lname = name.lower()

    # Strong hints from column name
    if any(k in lname for k in ["date", "time", "admit", "discharge", "collection"]):
        s_dt, is_dt = infer_datetime_series(s)
        if is_dt:
            return "datetime"

    if is_boolean_like(s):
        return "boolean"

    s_num, is_num = infer_numeric_series(s)
    if is_num:
        return "numeric"

    # Low cardinality object -> categorical
    if s.dtype == object:
        nunique = s.nunique(dropna=True)
        if nunique <= 50 or (len(s) > 0 and nunique / max(1, len(s)) < 0.05):
            return "categorical"
        return "text"

    # Fallback
    if s.dtype.kind in ("i", "u", "f"):
        return "numeric"
    if s.dtype.kind in ("M",):
        return "datetime"
    return str(s.dtype)


def summarize_column(name: str, s: pd.Series) -> ColumnSummary:
    role = infer_role(name, s)

    # Post-process conversions for summary stats only (do not mutate original df)
    s_for_stats = s
    if role == "datetime":
        s_for_stats, _ = infer_datetime_series(s_for_stats)
    elif role == "numeric":
        s_for_stats, _ = infer_numeric_series(s_for_stats)

    stats: Dict[str, float] = {}
    if role == "numeric":
        desc = s_for_stats.describe(percentiles=[0.05, 0.25, 0.5, 0.75, 0.95])
        stats = {
            "min": float(desc.get("min", np.nan)),
            "p05": float(desc.get("5%", np.nan)),
            "q1": float(desc.get("25%", np.nan)),
            "median": float(desc.get("50%", np.nan)),
            "q3": float(desc.get("75%", np.nan)),
            "p95": float(desc.get("95%", np.nan)),
            "max": float(desc.get("max", np.nan)),
            "mean": float(desc.get("mean", np.nan)),
            "std": float(desc.get("std", np.nan)),
        }
    elif role in ("categorical", "boolean"):
        vc = s.value_counts(dropna=False).head(15)
        for k, v in vc.items():
            stats[f"freq::{str(k)}"] = float(v)
    elif role == "datetime":
        # Convert to int timestamps for min/max
        try:
            sdt, _ = infer_datetime_series(s)
            stats = {
                "min_ts": float(pd.Timestamp(sdt.min())
                                 .to_pydatetime().timestamp()) if sdt.notna().any() else np.nan,
                "max_ts": float(pd.Timestamp(sdt.max())
                                 .to_pydatetime().timestamp()) if sdt.notna().any() else np.nan,
            }
        except Exception:
            stats = {}

    n_missing = int(s.isna().sum())
    pct_missing = float(n_missing / max(1, len(s)))
    n_unique = int(s.nunique(dropna=True))
    pct_unique = float(n_unique / max(1, len(s)))

    # Sample values for quick feel
    sample_values = [str(x) for x in s.dropna().unique()[:10]]

    return ColumnSummary(
        name=name,
        dtype=str(s.dtype),
        inferred_role=role,
        n_unique=n_unique,
        pct_unique=pct_unique,
        n_missing=n_missing,
        pct_missing=pct_missing,
        sample_values=sample_values,
        stats=stats,
    )


def detect_multiselect_groups(columns: List[str]) -> Dict[str, List[str]]:
    # Pattern: base___1, base___2, ...
    groups: Dict[str, List[str]] = {}
    pat = re.compile(r"^(.*)___\d+$")
    for col in columns:
        m = pat.match(col)
        if m:
            base = m.group(1)
            groups.setdefault(base, []).append(col)
    # Keep only groups with 2+
    groups = {k: sorted(v) for k, v in groups.items() if len(v) >= 2}
    return groups


def plot_numeric(series: pd.Series, name: str, out_dir: Path) -> Optional[Path]:
    s_num, is_num = infer_numeric_series(series)
    if not is_num:
        return None
    fig, ax = plt.subplots(figsize=(6, 4))
    try:
        s_num = s_num.dropna()
        if len(s_num) == 0:
            plt.close(fig)
            return None
        ax.hist(s_num, bins=30, color="#4C78A8")
        ax.set_title(f"Histogram: {name}")
        ax.set_xlabel(name)
        ax.set_ylabel("Count")
        out_path = out_dir / f"hist_{name}.png"
        fig.tight_layout()
        fig.savefig(out_path, dpi=150)
        plt.close(fig)
        return out_path
    except Exception:
        plt.close(fig)
        return None


def plot_categorical(series: pd.Series, name: str, out_dir: Path) -> Optional[Path]:
    if series.dtype != object and not is_boolean_like(series):
        return None
    vc = series.value_counts(dropna=False).head(15)
    if len(vc) == 0:
        return None
    fig, ax = plt.subplots(figsize=(7, 5))
    try:
        vc[::-1].plot(kind='barh', ax=ax, color="#72B7B2")
        ax.set_title(f"Top categories: {name}")
        ax.set_xlabel("Count")
        out_path = out_dir / f"bar_{name}.png"
        fig.tight_layout()
        fig.savefig(out_path, dpi=150)
        plt.close(fig)
        return out_path
    except Exception:
        plt.close(fig)
        return None


def extract_pdf_text(pdf_path: Path) -> str:
    if pdfplumber is None:
        return ""
    text_parts: List[str] = []
    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            for page in pdf.pages:
                txt = page.extract_text() or ""
                text_parts.append(txt)
    except Exception:
        return ""
    # Normalize whitespace
    text = "\n".join(text_parts)
    text = re.sub(r"\r", "\n", text)
    text = re.sub(r"\n+", "\n", text)
    return text


def search_codebook_hits(text: str, columns: List[str], groups: Dict[str, List[str]]) -> Dict[str, Dict[str, str]]:
    """
    Returns mapping: key -> {"type": "column"|"group", "match": <matched term>, "context": <surrounding text>}
    """
    if not text:
        return {}

    # Build a simple index of lines for context extraction
    lines = text.split("\n")
    line_text = [ln.strip() for ln in lines]

    hits: Dict[str, Dict[str, str]] = {}

    # Helper to find context around a term (exact or case-insensitive)
    def find_context(term: str, window: int = 2) -> Optional[Tuple[str, str]]:
        term_l = term.lower()
        # Exact line contains term (case-insensitive)
        for i, ln in enumerate(line_text):
            if term_l in ln.lower():
                start = max(0, i - window)
                end = min(len(line_text), i + window + 1)
                ctx = "\n".join(line_text[start:end]).strip()
                return (ln, ctx)
        return None

    # Search columns
    for col in columns:
        found = find_context(col)
        if found:
            hits[col] = {"type": "column", "match": found[0], "context": found[1]}

    # Search group prefixes too
    for base, cols in groups.items():
        # Try to find the base, and also sanitized form (replace underscores/spaces)
        candidates = [base, base.replace("_", " ").strip()]
        for term in candidates:
            found = find_context(term)
            if found:
                hits[base] = {"type": "group", "match": found[0], "context": found[1]}
                break

    return hits


def read_csv_with_fallback(path: Path) -> Tuple[pd.DataFrame, str]:
    """
    Try reading CSV with a set of common encodings to avoid UnicodeDecodeError.
    Returns (df, encoding_used).
    """
    encodings = ["utf-8", "utf-8-sig", "cp1252", "latin1"]
    last_err: Optional[Exception] = None
    for enc in encodings:
        try:
            df = pd.read_csv(path, low_memory=False, encoding=enc)
            return df, enc
        except UnicodeDecodeError as e:
            last_err = e
            continue
        except Exception as e:
            # Keep trying other encodings only if it's a decode error; otherwise re-raise.
            last_err = e
            continue
    if last_err is not None:
        raise last_err
    raise RuntimeError("Failed to read CSV with fallback encodings.")


def main():
    parser = argparse.ArgumentParser(description="Profile CSV and map columns to codebook PDF.")
    parser.add_argument("--csv_path", required=True, help="Path to the input CSV")
    parser.add_argument("--pdf_path", required=False, default=None, help="Path to the codebook PDF (optional)")
    parser.add_argument("--out_dir", required=False, default="data_profile_output", help="Output directory")
    parser.add_argument("--max_plots", type=int, default=60, help="Max number of plots across numeric/categorical columns")

    args = parser.parse_args()

    csv_path = Path(args.csv_path)
    pdf_path = Path(args.pdf_path) if args.pdf_path else None
    out_dir = Path(args.out_dir)

    if not csv_path.exists():
        print(f"ERROR: CSV not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    safe_mkdir(out_dir)
    plots_dir = out_dir / "plots"
    safe_mkdir(plots_dir)

    # Load CSV with minimal inference; keep data as-is
    print(f"Reading CSV: {csv_path}")
    df, enc_used = read_csv_with_fallback(csv_path)
    try:
        print(f"Detected encoding: {enc_used}")
    except Exception:
        pass

    n_rows, n_cols = df.shape
    mem_bytes = df.memory_usage(deep=True).sum()

    # Summaries
    col_summaries: List[ColumnSummary] = []
    for col in df.columns:
        col_summaries.append(summarize_column(col, df[col]))

    # Multiselect groups
    groups = detect_multiselect_groups(list(df.columns))

    # Save column profiles CSV
    profiles_csv = out_dir / "column_profiles.csv"
    prof_rows = []
    for cs in col_summaries:
        row = asdict(cs)
        # Flatten stats and sample_values for CSV
        for k, v in cs.stats.items():
            row[f"stat::{k}"] = v
        row["sample_values"] = " | ".join(cs.sample_values)
        prof_rows.append(row)
    pd.DataFrame(prof_rows).to_csv(profiles_csv, index=False)

    # Save summary JSON/MD
    summary = {
        "rows": int(n_rows),
        "columns": int(n_cols),
        "memory_bytes": int(mem_bytes),
        "memory_mb": float(mem_bytes / (1024 * 1024)),
        "multiselect_groups": groups,
        "columns": [asdict(cs) for cs in col_summaries],
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # Simple Markdown report
    md_lines = [
        f"# Data Profile Summary",
        "",
        f"- **Rows**: {n_rows}",
        f"- **Columns**: {n_cols}",
        f"- **Memory (MB)**: {summary['memory_mb']:.2f}",
        "",
        "## Multiselect Groups (prefix___N)",
    ]
    if groups:
        for k, v in groups.items():
            md_lines.append(f"- **{k}**: {len(v)} columns")
    else:
        md_lines.append("- None detected")

    md_lines.append("")
    md_lines.append("## Columns")
    for cs in col_summaries[:100]:  # limit to first 100 in MD for brevity
        md_lines.append(f"- **{cs.name}**: role={cs.inferred_role}, missing={cs.pct_missing:.1%}, unique={cs.n_unique}")

    (out_dir / "summary.md").write_text("\n".join(md_lines), encoding="utf-8")

    # Plots
    plot_count = 0
    # Numeric first
    for cs in col_summaries:
        if plot_count >= args.max_plots:
            break
        if cs.inferred_role == "numeric":
            p = plot_numeric(df[cs.name], cs.name, plots_dir)
            if p is not None:
                plot_count += 1
    # Then categorical/boolean
    for cs in col_summaries:
        if plot_count >= args.max_plots:
            break
        if cs.inferred_role in ("categorical", "boolean"):
            p = plot_categorical(df[cs.name], cs.name, plots_dir)
            if p is not None:
                plot_count += 1

    # Missingness bar (top 50)
    miss = df.isna().mean().sort_values(ascending=False).head(50)
    if len(miss) > 0:
        fig, ax = plt.subplots(figsize=(10, max(3, int(len(miss) * 0.25))))
        miss[::-1].plot(kind='barh', ax=ax, color="#E45756")
        ax.set_title("Top missingness by column (fraction)")
        ax.set_xlabel("Fraction missing")
        fig.tight_layout()
        fig.savefig(out_dir / "missingness_top50.png", dpi=150)
        plt.close(fig)

    # PDF codebook mapping
    codebook_hits: Dict[str, Dict[str, str]] = {}
    if pdf_path is not None and pdf_path.exists():
        if pdfplumber is None:
            print("WARNING: pdfplumber not installed; skipping PDF parsing.")
        else:
            print(f"Parsing codebook PDF: {pdf_path}")
            text = extract_pdf_text(pdf_path)
            codebook_hits = search_codebook_hits(text, list(df.columns), groups)
            (out_dir / "codebook_hits.json").write_text(json.dumps(codebook_hits, indent=2), encoding="utf-8")
            # Also save a Markdown view
            md = ["# Codebook Matches", ""]
            if not codebook_hits:
                md.append("No matches found or PDF text not extractable.")
            else:
                for key, rec in codebook_hits.items():
                    md.append(f"## {key} ({rec['type']})")
                    md.append("")
                    md.append("```")
                    md.append(rec.get("context", ""))
                    md.append("```")
                    md.append("")
            (out_dir / "codebook_hits.md").write_text("\n".join(md), encoding="utf-8")
    else:
        if pdf_path is not None:
            print(f"WARNING: PDF not found at {pdf_path}; skipping codebook parsing.")

    print("\nDone.")
    print(f"Output directory: {out_dir}")
    print(f"- column_profiles.csv, summary.json, summary.md")
    print(f"- plots in: {plots_dir}")
    if pdf_path is not None:
        print(f"- codebook_hits.json/md (if PDF was parsed)")


if __name__ == "__main__":
    main()
