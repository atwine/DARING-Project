# Step 5: Pilot Multiple Imputation & Diagnostics (Phase 2)

## Objective
Run a pilot Multiple Imputation consistent with the ML Implementation Plan to validate configuration, assess runtime, and generate diagnostics before final m=100 imputations.

## Inputs
- `../03_Variable_Classification/corrected_predictor_summary.csv`
- `../03_Variable_Classification/corrected_variable_selection.json`
- `../04_MICE_Setup/mice_config.json`
- Real data Excel: `../../Data/24 Oct 2025/GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx`

## Outputs
- `pilot_imputation_summary.json`
- `imputed_variables_distribution.csv` (means/SDs across m imputations for continuous vars)
- `pilot_imputed_sample_1.csv` (first 3 samples)
- `pilot_imputed_sample_2.csv`
- `pilot_imputed_sample_3.csv`
- `pilot_report.md` (with Interpretation)

## Notes
- Pilot m defaults to min(30, configured pilot m). Final analysis remains at m=100 (per Step 4 report).
- Categorical/binary variables are imputed with mode to keep pipeline simple and robust; continuous (and datetime → numeric) use IterativeImputer (MICE-like) with BayesianRidge and posterior sampling.
- Outcome `mortality` is included in the imputation predictor matrix but is not imputed.

## Run
- Use `run_pilot_imputation.bat`
