# Model Comparison Report
## DARING Project: Mortality Prediction in Bacterial Infections

**Analysis Date:** November 25, 2025  
**Analyst:** DARING Project Team  
**Status:** Complete

---

## Executive Summary

| Metric | Logistic Regression | Elastic Net | Random Forest |
|--------|---------------------|-------------|---------------|
| **C-statistic** | 0.779 (0.717-0.831) | 0.779 (0.717-0.831) | 0.954 (0.918-0.975) |
| **Calibration Slope** | 1.313 | 1.332 | 4.776 |
| **Brier Score** | 0.0868 | 0.0868 | 0.0687 |
| **Interpretable** | ✅ Yes | ✅ Yes | ❌ No |

### Selected Model: **Logistic Regression**

**Rationale:** Best calibration among all models (calibration slope 1.31, closest to ideal of 1.0). While Random Forest shows higher discrimination (C=0.95), its severely miscalibrated predictions (slope=4.78) make it unsuitable for clinical risk estimation.

---

## 1. Study Overview

### 1.1 Data Characteristics

| Parameter | Value |
|-----------|-------|
| **Sample Size** | 1,075 patients |
| **Events (Deaths)** | 128 (11.9%) |
| **Predictors** | 25 variables |
| **Imputed Datasets** | 100 (MICE with miceforest) |
| **Imputation Iterations** | 10 per dataset |

### 1.2 Pre-Specified Analysis Plan

Following TRIPOD guidelines and best practices (Collins et al., BMJ 2024), we pre-specified three candidate models **before examining any results**:

1. **Logistic Regression** — Primary model for interpretability
2. **Elastic Net** (α=0.5) — To handle potential predictor correlation
3. **Random Forest** (200 trees) — Benchmark for non-linear effects

### 1.3 Selection Criteria (Pre-Specified)

Applied in order of priority:
1. **Calibration slope** closest to 1.0
2. **C-statistic** (if calibration similar)
3. **Simplicity/interpretability** (if performance similar)

---

## 2. Model Results

### 2.1 Logistic Regression

```
C-statistic:        0.7790 (95% CI: 0.7168 - 0.8309)
Calibration Slope:  1.3132
Calibration Int.:   Estimated
Brier Score:        0.0868
```

**Interpretation:**
- **Discrimination**: Good (C > 0.75 indicates useful discrimination)
- **Calibration**: Slight overconfidence (slope > 1 means extreme predictions are slightly too extreme)
- **Clinical utility**: High — coefficients provide interpretable odds ratios

### 2.2 Elastic Net (Penalized Logistic)

```
C-statistic:        0.7790 (95% CI: 0.7166 - 0.8309)
Calibration Slope:  1.3322
Brier Score:        0.0868
```

**Interpretation:**
- Nearly identical to standard logistic regression
- Penalization did not substantially change results
- Suggests predictors are not highly collinear (shrinkage had minimal effect)

### 2.3 Random Forest

```
C-statistic:        0.9541 (95% CI: 0.9177 - 0.9748)
Calibration Slope:  4.7759
Brier Score:        0.0687
```

**Interpretation:**
- **Discrimination**: Excellent (C > 0.95)
- **Calibration**: **SEVERELY MISCALIBRATED** (slope >> 1)
- **Clinical utility**: Low — predictions cannot be trusted as probability estimates

⚠️ **Warning:** The high C-statistic of Random Forest is likely due to **overfitting**. The extreme calibration slope (4.78 instead of 1.0) indicates that:
- Predicted probabilities are overconfident
- A predicted 20% risk might actually correspond to only ~5% true risk
- Model memorized training data rather than learning generalizable patterns

---

## 3. Model Selection Analysis

### 3.1 Calibration Comparison

| Model | |Slope - 1.0| | Rank |
|-------|--------------|------|
| Logistic Regression | 0.313 | 🥇 1st |
| Elastic Net | 0.332 | 🥈 2nd |
| Random Forest | 3.776 | 🥉 3rd |

**Winner by calibration: Logistic Regression**

### 3.2 Why Not Choose Random Forest?

Despite RF's impressive C-statistic (0.95 vs 0.78), it was not selected because:

1. **Calibration is critical for clinical use**
   - A C-statistic tells us the model can *rank* patients by risk
   - Calibration tells us the predicted *probabilities* are accurate
   - For clinical decisions (e.g., "treat if risk > 20%"), calibration is essential

2. **Overfitting evidence**
   - C-statistic of 0.95 is suspiciously high for clinical prediction
   - Calibration slope of 4.78 confirms severe overfitting
   - After bootstrap correction, true performance would be much lower

3. **Black-box nature**
   - Cannot provide odds ratios for clinical interpretation
   - Harder to deploy and audit in clinical settings

### 3.3 Final Selection

✅ **Selected Model: Logistic Regression**

| Criterion | Assessment |
|-----------|------------|
| Calibration | Best (slope 1.31, closest to 1.0) |
| Discrimination | Good (C = 0.78, 95% CI: 0.72-0.83) |
| Interpretability | Excellent (odds ratios available) |
| Clinical deployment | Straightforward |

---

## 4. Clinical Interpretation

### 4.1 Model Performance in Context

| C-statistic | Interpretation |
|-------------|----------------|
| 0.5 | No discrimination (random) |
| 0.6-0.7 | Poor |
| **0.7-0.8** | **Acceptable/Good** ← Our model |
| 0.8-0.9 | Excellent |
| >0.9 | Outstanding (rare, check for overfitting) |

Our logistic regression model achieves **C = 0.779**, which is:
- Comparable to many established clinical prediction tools
- Appropriate for a mortality prediction model
- Realistic (not suspiciously high)

### 4.2 Calibration Slope Interpretation

| Slope | Meaning |
|-------|---------|
| < 1.0 | Predictions too moderate (underconfident) |
| **= 1.0** | **Perfect calibration** |
| > 1.0 | Predictions too extreme (overconfident) |

Our slope of 1.31 indicates:
- Model is slightly overconfident
- Recommended: Apply shrinkage factor (multiply coefficients by ~0.76) before deployment
- This is a normal finding that bootstrap validation will address

---

## 5. Methodological Notes

### 5.1 Pooling Methods

| Component | Method | Reference |
|-----------|--------|-----------|
| Coefficients | Rubin's rules | Rubin (1987) |
| Confidence intervals | Barnard-Rubin df adjustment | Barnard & Rubin (1999) |
| C-statistics | Logit transformation | Debray et al. (2017) |

### 5.2 Why Report All Models?

Following TRIPOD guidelines, we report results for **all pre-specified models**, not just the winner:

> "All candidate models should be reported, regardless of performance, to avoid publication bias and allow readers to evaluate the model development process."
> — Collins et al., BMJ 2024

### 5.3 Comparison to Literature

Typical C-statistics for mortality prediction models in hospitalized patients:

| Model | C-statistic | Reference |
|-------|-------------|-----------|
| APACHE II | 0.75-0.85 | Knaus et al. (1985) |
| SOFA | 0.70-0.80 | Vincent et al. (1996) |
| NEWS | 0.65-0.75 | Royal College of Physicians |
| **Our Model** | **0.78** | This study |

Our model's discrimination is **within the expected range** for clinical prediction tools.

---

## 6. Limitations

1. **Internal validation only** — External validation needed before clinical use
2. **Apparent performance** — Bootstrap optimism correction not yet applied
3. **Missing data** — High missingness in vital signs (60-85%), though handled via MICE
4. **Single-center** — Generalizability to other settings unknown

---

## 7. Next Steps

| Step | Description | Priority |
|------|-------------|----------|
| **Bootstrap validation** | Correct for optimism, apply shrinkage | High |
| **Coefficient interpretation** | Calculate and present odds ratios | High |
| **External validation** | Test on independent dataset | Critical |
| **Decision curve analysis** | Assess clinical utility at different thresholds | Medium |
| **Model presentation** | Create nomogram or risk calculator | Medium |

---

## 8. Conclusions

1. **Logistic regression was selected** as the final model based on pre-specified criteria
2. **C-statistic of 0.78** indicates good discrimination for mortality prediction
3. **Calibration slope of 1.31** suggests need for shrinkage before deployment
4. **Random Forest showed signs of overfitting** despite high apparent performance
5. **Pre-specified comparison strengthens validity** of model selection

---

## 9. References

1. Rubin DB (1987). Multiple Imputation for Nonresponse in Surveys. Wiley.
2. Barnard J, Rubin DB (1999). Small-sample degrees of freedom with multiple imputation. Biometrika 86(4):948-955.
3. Debray TPA et al. (2017). A guide to systematic review and meta-analysis of prediction model performance. BMJ 356:i6460.
4. Collins GS et al. (2024). Evaluation of clinical prediction models (part 1). BMJ 384:e074819.
5. Steyerberg EW (2019). Clinical Prediction Models, 2nd Edition. Springer.
6. TRIPOD+AI Statement (2024). BMJ 385:e078378.

---

## Appendix: Output Files

| File | Description |
|------|-------------|
| `model_comparison.csv` | Performance metrics for all models |
| `model_comparison.png` | ROC curves and calibration plots |
| `model_results.json` | Complete results in JSON format |
| `logistic_coefficients.csv` | Pooled coefficients for logistic regression |

---

*Report generated: November 25, 2025*
*DARING Project — Mortality Prediction Model Development*
