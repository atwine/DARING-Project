# Step 3 Report: Variable Classification and Selection

Analysis Date: 2025-11-04 15:14

## Outcome (Target)
- Variable: `mortality` (0=survived, 1=died)
- Events: 124 (11.5%)
- Suitable for modeling: Yes

## Selected Predictors (15–25 per ML Plan)
- Count: 25

| Variable | Category | Type | Missing % | Evidence | Justification |
|---|---|---|---:|---|---|
| `age` | Demographics | continuous | 0.1 | Strong | Age is a consistently strong predictor of mortality across infections. |
| `sex` | Demographics | binary | 0.0 | Strong | Sex differences affect immune response and health-seeking behavior. |
| `ward` | Clinical_Severity | categorical | 0.1 | Strong | Ward type proxies acuity and monitoring intensity (ICU vs general). |
| `systolic_bp_baseline` | Vital_Signs | continuous | 57.8 | Strong | Hypotension is a key sepsis severity marker. |
| `hiv_status` | Comorbidities | categorical | 0.1 | Strong | Immunosuppression increases risk of severe infection and death. |
| `cormobid_condition` | Comorbidities | binary | 0.0 | Strong | Comorbidity burden increases mortality risk. |
| `pulse_baseline` | Vital_Signs | continuous | 57.2 | Moderate | Tachycardia reflects physiologic stress and infection severity. |
| `temp_baseline` | Vital_Signs | continuous | 84.7 | Moderate | Fever patterns correlate with systemic inflammatory response. |
| `rr_baseline` | Vital_Signs | continuous | 86.2 | Moderate | Tachypnea indicates respiratory compromise and sepsis. |
| `spo2_baseline` | Vital_Signs | continuous | 66.7 | Moderate | Hypoxemia associates with adverse outcomes. |
| `gcs_baseline` | Vital_Signs | continuous | 95.1 | Moderate | Neurologic depression signals critical illness risk. |
| `first_organism` | Infection | categorical | 46.9 | Moderate | Pathogen virulence profiles differ in mortality risk. |
| `infect_site___1` | Infection | categorical | 0.0 | Moderate | Infection site (e.g., bloodstream) has distinct risk profiles. |
| `referral` | Clinical_Process | binary | 0.2 | Moderate | Referral captures delayed presentation and higher severity. |
| `facility_category` | System | categorical | 80.0 | Moderate | System capacity and resources vary by facility level. |
| `name_of_rrh` | System | categorical | 0.0 | Moderate | Facility-specific effects (case-mix, protocols) influence outcomes. |
| `complications` | Clinical_Severity | binary | 0.0 | Moderate | Complications reflect disease severity and clinical deterioration. |
| `admission_date` | Clinical_Process | datetime | 0.1 | Weak | Seasonality and system load can affect outcomes. |
| `res_district` | Demographics | categorical | 5.3 | Weak | Geography proxies access to care and socioeconomic context. |
| `occupation` | Demographics | categorical | 78.2 | Weak | Socioeconomic factors influence baseline risk. |
| `allergies` | Clinical_History | categorical | 0.0 | Weak | Clinical history marker; weak predictor, possible auxiliary utility. |
| `antib_prior_admi` | Clinical_History | binary | 0.1 | Weak | Prior antibiotics affect resistance and outcomes. |
| `infect_site___2` | Infection | categorical | 0.0 | Weak | Additional infection site information refines risk. |
| `infect_site___3` | Infection | categorical | 0.0 | Weak | Additional infection site information refines risk. |
| `site_based_sample___1` | Infection | categorical | 0.0 | Weak | Specimen type supports infection source classification. |

## Methodology
- Followed van Buuren criteria: 15–25 variables for imputation models (per ML Plan, Step 1.2).
- Outcome included in imputation models; predictors chosen by evidence, priority, and missingness.

## Next
- Proceed to Phase 2: MICE configuration using selected predictors and auxiliary variables.