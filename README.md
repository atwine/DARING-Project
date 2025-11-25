# DARING Project
## Mortality Prediction in Bacterial Infections - Uganda Multi-Site Study

**GHS-CAMO-Net Project 3**

---

## Overview

This project develops a **clinical prediction model for mortality in patients with bacterial infections** across multiple hospitals in Uganda. The model uses readily available clinical data to identify high-risk patients who may benefit from intensified care.

## Key Results

| Metric | Value |
|--------|-------|
| **Sample Size** | 1,075 patients |
| **Mortality Rate** | 11.5% (124 deaths) |
| **Final Model** | Logistic Regression |
| **C-statistic** | 0.78 (95% CI: 0.72-0.83) |
| **Optimism-Corrected C** | 0.73 |

## Project Structure

```
DARING Project/
├── Data/                           # Raw and processed data
├── Plan/                           # Analysis pipeline
│   ├── 01_Real_vs_Synthetic_Comparison/
│   ├── 02_Data_Quality_Audit/
│   ├── 03_Variable_Classification/
│   ├── 04_MICE_Setup/
│   ├── 05_MICE_Pilot_Imputation/
│   ├── 06_Final_Imputation/
│   ├── 07_Model_Development/
│   └── 08_Final_Reports/
└── scripts/                        # Utility scripts
```

## Methodology

1. **Data Quality Audit** - Comprehensive missing data assessment
2. **Variable Classification** - Evidence-based predictor selection (25 variables)
3. **Multiple Imputation** - MICE with 100 imputed datasets (miceforest)
4. **Model Comparison** - Pre-specified comparison of Logistic Regression, Elastic Net, Random Forest
5. **Internal Validation** - Bootstrap validation (200 resamples)

## Statistical Methods

- **Missing Data**: Multiple Imputation by Chained Equations (MICE)
- **Pooling**: Rubin's Rules with Barnard-Rubin df adjustment
- **C-statistic Pooling**: Logit transformation (Debray et al., 2017)
- **Validation**: Bootstrap optimism correction (Harrell, 2015)

## Top Predictors of Mortality

1. Presence of comorbidities
2. Glasgow Coma Scale (lower = higher risk)
3. Age (older = higher risk)
4. Infection site
5. Presence of complications

## Requirements

- Python 3.10+
- pandas, numpy, scikit-learn
- miceforest
- matplotlib

## Status

- ✅ Model Development Complete
- ⏳ External Validation Pending

## References

- Rubin DB (1987). Multiple Imputation for Nonresponse in Surveys
- Steyerberg EW (2019). Clinical Prediction Models, 2nd Edition
- Collins GS et al. (2024). Evaluation of clinical prediction models. BMJ
- TRIPOD+AI Statement (2024). BMJ

## License

This project is for research purposes.

---

*DARING Project — GHS-CAMO-Net Project 3*
