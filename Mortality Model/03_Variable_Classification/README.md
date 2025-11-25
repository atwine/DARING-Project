# Step 3: Variable Classification and Selection (Phase 1, Step 1.2)

## 📋 **Objective**
Systematic classification of variables for mortality prediction modeling, following ML Implementation Plan Phase 1, Step 1.2.

## 🎯 **Goals (Per ML Implementation Plan)**
1. **Predictor Variable Selection:** Choose 15-25 variables for mortality prediction (per van Buuren's criteria)
2. **Auxiliary Variable Identification:** Select variables to improve MICE imputation
3. **Variable Type Classification:** Continuous, binary, categorical, ordinal
4. **Missing Data Mechanism:** Document per-variable missingness reasons
5. **Clinical Justification:** Provide evidence-based rationale for selections
6. **Imputation Method Assignment:** Specify MICE method per variable type

## 📊 **Input from Previous Steps**
- **Mortality Events:** 124 deaths (sufficient for 15-25 predictors per ML Plan)
- **Missing Mechanism:** MAR/MNAR confirmed
- **Complete Cases:** 53% for core predictors
- **Variable Pool:** 487 usable variables (low + complete missing categories)

## 📁 **Expected Outputs**
- Predictor variable selection with clinical justification
- Auxiliary variable identification for imputation enhancement  
- Variable classification table (type, missing %, mechanism)
- MICE imputation method assignment
- Clinical literature support for selections
- TRIPOD+AI Item 10 compliance documentation

## 🎯 **Success Criteria**
- [ ] 15-25 predictor variables selected (per ML Implementation Plan)
- [ ] Each selection clinically justified with literature
- [ ] Auxiliary variables identified for imputation improvement
- [ ] Variable types classified for MICE setup
- [ ] Missing data mechanisms documented per variable
- [ ] Imputation methods assigned based on variable characteristics

## 🔬 **Variable Selection Principles (Per ML Implementation Plan)**
1. **Van Buuren's Criteria:** 15-25 variables for imputation models
2. **Clinical Relevance:** Evidence-based mortality predictors
3. **Data Quality:** Prioritize lower missing rates
4. **Practical Utility:** Available in real clinical settings
5. **Collinearity Avoidance:** Select non-redundant predictors
6. **Generalizability:** Applicable across similar settings

---
**Phase:** 1 - Data Preparation  
**Step:** 1.2 - Variable Classification and Selection  
**Focus:** Mortality Prediction with MICE Preparation
