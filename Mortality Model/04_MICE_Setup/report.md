# Phase 2: MICE Setup Report (Step 2.1–2.3)

Analysis Date: 2025-11-04 15:22

## Outcome and Variable Scope
- Outcome (included in imputation models): `mortality`
- Predictors selected: 25
- Predictors available in data: 25

## Missingness Summary
- Variables to impute: 16
- Percent incomplete cases (any missing among predictors): 100.0%

## Imputation Counts (per ML Plan)
- Minimum (White's rule): m = 100
- Pilot analysis: m = 100
- Final analysis: m = 100

## MICE Methods by Variable
| Variable | Type | Method | Missing % |
|---|---|---|---:|
| `age` | continuous | pmm | 0.1 |
| `sex` | binary | logreg | 0.0 |
| `ward` | categorical | polyreg | 0.1 |
| `systolic_bp_baseline` | continuous | pmm | 57.8 |
| `hiv_status` | categorical | polyreg | 0.1 |
| `cormobid_condition` | binary | logreg | 0.0 |
| `pulse_baseline` | continuous | pmm | 57.2 |
| `temp_baseline` | continuous | pmm | 84.7 |
| `rr_baseline` | continuous | pmm | 86.2 |
| `spo2_baseline` | continuous | pmm | 66.7 |
| `gcs_baseline` | continuous | pmm | 95.1 |
| `first_organism` | categorical | polyreg | 46.9 |
| `infect_site___1` | categorical | polyreg | 0.0 |
| `referral` | binary | logreg | 0.2 |
| `facility_category` | categorical | polyreg | 80.0 |
| `name_of_rrh` | categorical | polyreg | 0.0 |
| `complications` | binary | logreg | 0.0 |
| `admission_date` | datetime | pmm | 0.1 |
| `res_district` | categorical | polyreg | 5.3 |
| `occupation` | categorical | polyreg | 78.2 |
| `allergies` | categorical | polyreg | 0.0 |
| `antib_prior_admi` | binary | logreg | 0.1 |
| `infect_site___2` | categorical | polyreg | 0.0 |
| `infect_site___3` | categorical | polyreg | 0.0 |
| `site_based_sample___1` | categorical | polyreg | 0.0 |

## Predictor Matrix
- imputation_matrix.csv contains the 0/1 inclusion for each imputed variable; outcome included for all.