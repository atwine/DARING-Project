# Step 4: MICE Setup (Phase 2, Step 2.1–2.3)

## Objective
Prepare imputation configuration for mortality modeling using MICE, adhering to the ML Implementation Plan (van Buuren criteria, TRIPOD+AI).

## Goals
- Compute number of imputations (pilot and final) per ML Plan guidance.
- Build variable lists for imputation (include outcome `mortality` in predictor matrices; do not impute it).
- Assign MICE methods by variable type (PMM, logistic, multinomial, datetime→numeric).
- Generate configuration artifacts for the next step:
  - `mice_config.json`
  - `imputation_matrix.csv`
  - `setup_report.md`

## Inputs
- Step 3 outputs:
  - `03_Variable_Classification/corrected_variable_selection.json`
  - `03_Variable_Classification/corrected_predictor_summary.csv`
- Real dataset: `Data/24 Oct 2025/GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx`

## Expected Outputs
- Imputation counts: pilot m and final m justified by incomplete-case rate.
- Predictor matrix including `mortality` for all imputed variables.
- Clear report detailing assumptions and references.

## Run
- Use: `run_mice_setup.bat`
