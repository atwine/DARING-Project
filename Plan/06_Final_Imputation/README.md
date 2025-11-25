# Step 6: Final Multiple Imputation (Phase 2)

## Objective
Run the final Multiple Imputation using miceforest (m=100) with proper PMM for continuous variables and native categorical handling.

## Method
- **Library**: miceforest (LightGBM with Predictive Mean Matching)
- **PMM Donor Pool**: 5 candidates (per ML Plan Step 2.2)
- **Iterations**: 20 (per ML Plan Step 2.3)
- **Imputations**: m=100 (per White's rule, Step 4)
- **Clinical Bounds**: Enforced per ML Plan Step 2.5

## Inputs
- `../03_Variable_Classification/corrected_predictor_summary.csv`
- `../03_Variable_Classification/corrected_variable_selection.json`
- `../04_MICE_Setup/mice_config.json`
- Real data: `../../Data/24 Oct 2025/GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx`

## Outputs
- `miceforest_summary.json` - Complete summary with validation results
- `miceforest_distributions.csv` - Distribution statistics across imputations
- `miceforest_sample_1.csv` - Sample dataset for inspection
- `miceforest_sample_2.csv`
- `miceforest_sample_3.csv`
- `miceforest_report.md` - Final report

## Prerequisites
```bash
pip install miceforest
```

## Run
```bash
python miceforest_imputation.py
```

## Notes
- miceforest properly handles categorical variables (no negative float issues)
- PMM ensures imputed values come from observed data distribution
- Clinical bounds are enforced post-imputation as safety net
- Outcome `mortality` is included as predictor but never imputed
