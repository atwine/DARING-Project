# Step 7: Model Development (Phase 3)

## Objective
Develop and compare clinical prediction models for mortality using multiply imputed datasets, following TRIPOD guidelines and best practices.

---

## Methodological Rationale

### Why Multi-Model Comparison?

We compare **three pre-specified models** rather than using a single model or data-driven selection:

| Approach | Problem | Our Solution |
|----------|---------|--------------|
| Single model only | May miss better alternatives | Compare 3 candidates |
| Data-driven selection | Inflates optimism, selection bias | Pre-specify before results |
| Report only "winner" | Publication bias | Report ALL results |

### Pre-Specified Models

#### 1. Logistic Regression (Primary)
- **Why**: Gold standard for clinical prediction, interpretable coefficients
- **Clinical value**: "Each unit increase in X changes mortality odds by Y%"
- **Pooling**: Full Rubin's rules on coefficients

#### 2. Elastic Net (α=0.5)
- **Why**: Handles correlated predictors (vital signs often correlated)
- **Clinical value**: More stable when predictors have multicollinearity
- **Pooling**: Rubin's rules on coefficients

#### 3. Random Forest (200 trees)
- **Why**: Captures non-linear effects & interactions automatically
- **Clinical value**: Benchmark - if similar to LR, linear model is adequate
- **Pooling**: Pool predictions, then compute metrics

### Selection Criteria (Pre-Specified)

Applied in order:
1. **Calibration slope** closest to 1.0 (well-calibrated predictions)
2. **C-statistic** (if calibration similar within 0.1)
3. **Simplicity** (if performance within 0.02 AUC, prefer logistic regression)

### Why This Order?
- **Calibration > Discrimination**: A well-calibrated model is more useful clinically than one with high AUC but poor calibration
- **Simplicity matters**: Interpretable models are preferred for clinical deployment

---

## Statistical Methods

### Rubin's Rules for Pooling
```
Pooled estimate: Q̄ = (1/m) Σ Qᵢ
Within variance:  Ū = (1/m) Σ Uᵢ
Between variance: B = Var(Qᵢ)
Total variance:   T = Ū + (1 + 1/m)B
```

### C-Statistic Pooling
- **Method**: Logit transformation before pooling (Debray et al., BMJ 2016)
- **Rationale**: C-statistic is bounded [0.5, 1], requires transformation for valid CI

### Calibration Assessment
- **Calibration slope**: From logistic regression of outcome on log-odds of predictions
- **Ideal**: Slope = 1.0, Intercept = 0.0

---

## Inputs
- `../06_Final_Imputation/imputed_data/imputed_dataset_*.csv` - Imputed datasets

## Outputs
- `model_comparison.csv` - Comparison table (all 3 models)
- `model_comparison.png` - ROC curves and calibration plots
- `model_results.json` - Detailed results with selection reasoning
- `logistic_coefficients.csv` - Pooled coefficients for logistic regression

## Run
```bash
python model_comparison.py
```

---

## References

1. **Rubin DB** (1987). Multiple Imputation for Nonresponse in Surveys. Wiley.
2. **Barnard J, Rubin DB** (1999). Small-sample degrees of freedom with multiple imputation. Biometrika 86(4):948-955.
3. **Debray TPA et al.** (2017). A guide to systematic review and meta-analysis of prediction model performance. BMJ 356:i6460.
4. **Collins GS et al.** (2024). Evaluation of clinical prediction models (part 1). BMJ 384:e074819.
5. **Steyerberg EW** (2019). Clinical Prediction Models, 2nd Edition. Springer.
6. **TRIPOD+AI Statement** (2024). BMJ 385:e078378.

---

## Why NOT Data-Driven Model Selection?

> "We advise against... stepwise methods for variable selection... they might lead to bias in estimation and worse predictive performance."
> — Collins et al., BMJ 2024

**Problems with testing many models and picking the best:**
1. **Selection bias**: Same data used to select AND evaluate
2. **Inflated optimism**: Each comparison increases overfitting risk
3. **MI conflict**: "Best" model may differ across imputations
4. **Publication bias**: Unreported models create false impression

**Our approach ensures:**
- Transparent, reproducible methodology
- All results reported regardless of outcome
- Selection criteria independent of performance metrics
