# Synthetic Data Generation (GHS-CAMO-Net Project 3)

This document records how the synthetic dataset and reports were generated so anyone can reproduce the process.

## Overview
- Source data: `C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025\GHS-CAMO-Net Project 3.csv`
- Script used: `C:\Users\ic\OneDrive\Desktop\DARING Project\scripts\synthesize_data.py`
- Outputs written here:
  - `synthetic_output.csv` (synthetic data)
  - `quality_report.json` (SDMetrics Single Table QualityReport)
  - `privacy_report.json` (placeholder if PrivacyReport is unavailable in current sdmetrics)

## Environment
- OS: Windows
- Python: 3.12 (venv located in project root as `.venv`)
- Key packages:
  - SDV (single-table GaussianCopulaSynthesizer)
  - SDMetrics (QualityReport; PrivacyReport may be absent in 0.23+)
- Install/upgrade (inside the venv):
  ```bash
  python -m pip install -U sdv sdmetrics
  # (If needed)
  python -m pip install -U rdt copulas
  ```
- Record versions for provenance:
  ```bash
  python -m pip show sdv sdmetrics rdt copulas
  ```

## Reproducibility
- The script seeds Python and NumPy RNGs via `--random_seed`.
- For the installed SDV (1.x), `synth.sample()` does not accept `random_state`; global seeding ensures deterministic samples.

## Full run (complete dataset)
Use Git Bash or PowerShell/CMD (single line). Paths below are absolute.

```bash
python "C:\Users\ic\OneDrive\Desktop\DARING Project\scripts\synthesize_data.py" \
  --input "C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025\GHS-CAMO-Net Project 3.csv" \
  --output_csv "C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025\Synthetic Data\synthetic_output.csv" \
  --quality_json "C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025\Synthetic Data\quality_report.json" \
  --privacy_json "C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025\Synthetic Data\privacy_report.json" \
  --rows 0 \
  --drop_text_high_card \
  --exclude_columns rec_id patient_id \
  --random_seed 42
```

Notes:
- `--rows 0` generates the same number of rows as the filtered real data.
- `--drop_text_high_card` removes very high-cardinality text columns to improve model fit and metrics.
- `--exclude_columns rec_id patient_id` excludes explicit identifiers.
- Quality and privacy JSONs are saved alongside the synthetic CSV in this folder.

## Quick test (fast validation before full run)
To avoid long waits, you can run a smaller test to verify the pipeline.

```bash
python "C:\Users\ic\OneDrive\Desktop\DARING Project\scripts\synthesize_data.py" \
  --input "C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025\GHS-CAMO-Net Project 3.csv" \
  --output_csv "C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025\Synthetic Data\synthetic_output_quick.csv" \
  --quality_json "C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025\Synthetic Data\quality_report_quick.json" \
  --privacy_json "C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025\Synthetic Data\privacy_report_quick.json" \
  --rows 200 \
  --drop_text_high_card \
  --exclude_columns rec_id patient_id \
  --limit_rows_real 500 \
  --limit_columns 40 \
  --random_seed 42
```

- `--limit_rows_real` restricts the number of real rows learned to speed up fitting.
- `--limit_columns` reduces the number of columns to keep SDMetrics pairwise metrics fast (pairwise is O(M^2)).
- `--skip_quality` can be added to skip the SDMetrics reports entirely for the quickest smoke test.

## Parameters used in the successful full run
- `--rows 0`
- `--drop_text_high_card`
- `--exclude_columns rec_id patient_id`
- `--random_seed 42`

Quality outcome observed (example):
- Column Shapes: ~95%
- Column Pair Trends: ~98%
- Overall Quality: ~97%

Actual values depend on data and environment; see `quality_report.json`.

## Outputs
- `synthetic_output.csv`: Synthetic dataset.
- `quality_report.json`: Contains `overall_score` and `properties` (table of component scores).
- `privacy_report.json`:
  - If `PrivacyReport` is available in sdmetrics, a score and details are included.
  - If not, the script writes a placeholder with `overall_score: null` and a note.

## Troubleshooting
- CSV encoding errors: the script tries encodings in order (`utf-8`, `utf-8-sig`, `cp1252`, `latin1`).
- SDMetrics metadata type error: script passes `metadata.to_dict()` to SDMetrics APIs (required).
- Long runtime: Column Pair Trends is quadratic in the number of columns. Use quick test flags first.
- Datetime parsing warning: you may set a format using SDV metadata if needed.
- Deprecation warnings: `SingleTableMetadata` is deprecated in newer SDV; the script remains compatible.

## References
- SDV GaussianCopulaSynthesizer: https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/gaussiancopulasynthesizer
- SDMetrics Single Table Quality Report: https://docs.sdv.dev/sdmetrics/reports/quality-report/single-table-api

## Provenance and Change Log
- Created on: 2025-10-27
- Script revision: supports optional PrivacyReport, metadata dict conversion for SDMetrics, reproducible seeding, and quick-test flags (`--limit_rows_real`, `--limit_columns`, `--skip_quality`).
