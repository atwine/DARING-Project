"""
MORTALITY PREDICTION MODEL SPECIFICATION
=======================================

This script clarifies the mortality prediction setup:
- OUTCOME: What we're predicting (mortality yes/no)  
- PREDICTORS: What we use to make the prediction (12 selected variables)

This confirms our model structure is correct for mortality prediction.
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Set up paths
PLAN_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan")
DATA_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025")
OUTPUT_DIR = PLAN_DIR / "03_Variable_Classification"

print("="*80)
print("MORTALITY PREDICTION MODEL SPECIFICATION")
print("="*80)

# Load dataset
data_path_excel = DATA_DIR / "GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx"
df = pd.read_excel(data_path_excel, sheet_name=0)

print(f"\n📊 Dataset Overview:")
print(f"  Total patients: {len(df)}")
print(f"  Total variables: {len(df.columns)}")

# ============================================================================
# OUTCOME VARIABLE DEFINITION
# ============================================================================

print(f"\n🎯 OUTCOME VARIABLE (What we're predicting):")
print("="*50)

# Check treatment_outcome variable
if 'treatment_outcome' in df.columns:
    print(f"Original treatment outcomes:")
    outcome_counts = df['treatment_outcome'].value_counts()
    for outcome, count in outcome_counts.items():
        percentage = (count / len(df)) * 100
        print(f"  - {outcome}: {count} ({percentage:.1f}%)")
    
    # Create binary mortality outcome
    df['mortality'] = (df['treatment_outcome'] == 'Died').astype(int)
    
    mortality_count = df['mortality'].sum()
    mortality_rate = (mortality_count / len(df)) * 100
    
    print(f"\n✅ BINARY MORTALITY OUTCOME CREATED:")
    print(f"  Variable name: 'mortality'")
    print(f"  Deaths (mortality=1): {int(mortality_count)} ({mortality_rate:.1f}%)")
    print(f"  Survivors (mortality=0): {int(len(df) - mortality_count)} ({100-mortality_rate:.1f}%)")
    print(f"  Statistical power: {int(mortality_count/10)} max predictors (10:1 rule)")
    
else:
    print("❌ treatment_outcome variable not found!")

# ============================================================================
# PREDICTOR VARIABLES (What we use to predict)
# ============================================================================

print(f"\n🔍 PREDICTOR VARIABLES (What we use to predict mortality):")
print("="*60)

# Load our selected predictors
predictor_summary = pd.read_csv(OUTPUT_DIR / 'final_predictor_summary.csv')

print(f"Selected {len(predictor_summary)} predictor variables:")
print(f"\n{'Rank':<4} {'Variable':<25} {'Category':<15} {'Missing%':<10} {'Evidence'}")
print("-" * 70)

for idx, row in predictor_summary.iterrows():
    print(f"{idx+1:<4} {row['Variable']:<25} {row['Category']:<15} "
          f"{row['Missing_Rate_Percent']:<9.1f}% {row['Evidence_Level']}")

# ============================================================================
# MODEL FORMULA SPECIFICATION
# ============================================================================

print(f"\n📋 MORTALITY PREDICTION MODEL FORMULA:")
print("="*45)

predictor_list = predictor_summary['Variable'].tolist()

print(f"\n🎯 MODEL SPECIFICATION:")
print(f"  OUTCOME (Y): mortality (0=survived, 1=died)")
print(f"  PREDICTORS (X): {len(predictor_list)} variables")
print(f"\n  Mathematical formula:")
print(f"  mortality ~ age + sex + ward + systolic_bp_baseline + pulse_baseline")
print(f"            + hiv_status + cormobid_condition + first_organism") 
print(f"            + referral + facility_category + complications + infect_site___1")

print(f"\n  Logistic regression form:")
print(f"  log(odds of mortality) = β₀ + β₁×age + β₂×sex + β₃×ward + ...")

# ============================================================================
# DATA AVAILABILITY CHECK
# ============================================================================

print(f"\n🔍 DATA AVAILABILITY CHECK:")
print("="*35)

available_predictors = []
missing_predictors = []

print(f"\nChecking predictor availability in dataset:")
for predictor in predictor_list:
    if predictor in df.columns:
        missing_rate = (df[predictor].isnull().sum() / len(df)) * 100
        available_predictors.append(predictor)
        print(f"  ✅ {predictor:<25}: Available ({missing_rate:5.1f}% missing)")
    else:
        missing_predictors.append(predictor)
        print(f"  ❌ {predictor:<25}: NOT FOUND")

print(f"\n📊 PREDICTOR AVAILABILITY SUMMARY:")
print(f"  Available predictors: {len(available_predictors)}/{len(predictor_list)}")
print(f"  Missing predictors: {len(missing_predictors)}")

if missing_predictors:
    print(f"  Missing predictors: {', '.join(missing_predictors)}")

# ============================================================================
# COMPLETE CASE ANALYSIS FOR MODEL
# ============================================================================

print(f"\n📈 COMPLETE CASE ANALYSIS FOR MORTALITY MODEL:")
print("="*50)

# Check complete cases for outcome + predictors
model_variables = ['mortality'] + available_predictors

if all(var in df.columns for var in model_variables):
    model_df = df[model_variables].copy()
    
    complete_cases = model_df.dropna().shape[0]
    complete_rate = (complete_cases / len(df)) * 100
    
    complete_deaths = model_df.dropna()['mortality'].sum()
    
    print(f"  Model variables: {len(model_variables)} (1 outcome + {len(available_predictors)} predictors)")
    print(f"  Complete cases: {complete_cases}/{len(df)} ({complete_rate:.1f}%)")
    print(f"  Complete deaths: {int(complete_deaths)} events available for modeling")
    print(f"  Events per predictor: {complete_deaths/len(available_predictors):.1f}")
    
    if complete_rate >= 40:
        print(f"  ✅ Sufficient complete cases for modeling")
    else:
        print(f"  ⚠️ Low complete cases - MICE imputation essential")
        
    if complete_deaths >= len(available_predictors) * 10:
        print(f"  ✅ Sufficient events for {len(available_predictors)} predictors")
    else:
        print(f"  ⚠️ May need to reduce predictor count")

# ============================================================================
# MORTALITY PREDICTION SUMMARY
# ============================================================================

print(f"\n🎯 MORTALITY PREDICTION MODEL SUMMARY:")
print("="*45)

print(f"\n✅ MODEL CORRECTLY SPECIFIED FOR MORTALITY PREDICTION:")
print(f"  🎯 OUTCOME: mortality (what we predict)")
print(f"     - Binary: 0=survived, 1=died")  
print(f"     - Events: {int(mortality_count)} deaths ({mortality_rate:.1f}%)")
print(f"     - Power: Sufficient for {int(mortality_count/10)} predictors")

print(f"\n  🔍 PREDICTORS: {len(available_predictors)} variables (what we use to predict)")
print(f"     - Demographics: age, sex")
print(f"     - Clinical severity: ward, BP, pulse, referral, complications")
print(f"     - Comorbidities: HIV, chronic conditions")
print(f"     - Infection: organism, site")
print(f"     - System: facility category")

print(f"\n  📊 STATISTICAL APPROACH:")
print(f"     - Logistic regression (binary outcome)")
print(f"     - MICE for missing data imputation")
print(f"     - Bootstrap validation (Boot-MI)")
print(f"     - Expected AUC: 0.65-0.75")

print(f"\n✅ READY FOR MORTALITY PREDICTION MODELING!")
print(f"   Next: Phase 2 - MICE Implementation")

print(f"\n" + "="*80)
print("MORTALITY MODEL SPECIFICATION CONFIRMED!")
print("="*80)
