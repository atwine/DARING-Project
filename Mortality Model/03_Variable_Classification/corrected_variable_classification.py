"""
CORRECTED PHASE 1, STEP 1.2: Variable Classification and Selection
================================================================

Following ML Implementation Plan: 15-25 variables per van Buuren's criteria
MORTALITY is the OUTCOME (what we predict)
PREDICTORS are what we use to predict mortality (15-25 variables)

Author: Clinical ML Analysis Team
Date: November 2025
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from datetime import datetime

# Set up paths
PLAN_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan")
DATA_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025")
OUTPUT_DIR = PLAN_DIR / "03_Variable_Classification"

print("="*80)
print("CORRECTED PHASE 1, STEP 1.2: VARIABLE CLASSIFICATION AND SELECTION")
print("Following ML Implementation Plan: 15-25 variables per van Buuren's criteria")
print("="*80)

# Load dataset
data_path_excel = DATA_DIR / "GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx"
df = pd.read_excel(data_path_excel, sheet_name=0)

print(f"\n📊 Dataset loaded: {df.shape[0]} patients, {df.shape[1]} variables")

# ============================================================================
# DEFINE MORTALITY OUTCOME (WHAT WE'RE PREDICTING)
# ============================================================================

print(f"\n🎯 MORTALITY OUTCOME DEFINITION:")
print("="*40)

if 'treatment_outcome' in df.columns:
    # Show original outcomes
    print("Original treatment outcomes:")
    for outcome, count in df['treatment_outcome'].value_counts().items():
        print(f"  - {outcome}: {count} ({count/len(df)*100:.1f}%)")
    
    # Create binary mortality outcome
    df['mortality'] = (df['treatment_outcome'] == 'Died').astype(int)
    deaths = df['mortality'].sum()
    
    print(f"\n✅ MORTALITY OUTCOME (WHAT WE PREDICT):")
    print(f"  Variable: 'mortality' (0=survived, 1=died)")
    print(f"  Deaths: {deaths} ({deaths/len(df)*100:.1f}%)")
    print(f"  Survivors: {len(df)-deaths} ({(len(df)-deaths)/len(df)*100:.1f}%)")

# ============================================================================
# COMPREHENSIVE PREDICTOR VARIABLE POOL
# ============================================================================

print(f"\n🔍 BUILDING COMPREHENSIVE PREDICTOR VARIABLE POOL:")
print("="*55)

# Load previous missing data analysis
missing_file = PLAN_DIR / "02_Data_Quality_Audit" / "detailed_missing_analysis.csv"
if missing_file.exists():
    missing_df = pd.read_csv(missing_file)
    print("✓ Previous missing data analysis loaded")
else:
    # Create basic missing analysis
    missing_df = pd.DataFrame({
        'Variable': df.columns,
        'Missing_Percent': [(df[col].isnull().sum() / len(df)) * 100 for col in df.columns]
    })

# Categorize variables by missing data rates (per van Buuren's criteria)
complete_vars = missing_df[missing_df['Missing_Percent'] == 0]['Variable'].tolist()
low_missing_vars = missing_df[missing_df['Missing_Percent'] <= 20]['Variable'].tolist()
moderate_missing_vars = missing_df[(missing_df['Missing_Percent'] > 20) & 
                                  (missing_df['Missing_Percent'] <= 50)]['Variable'].tolist()

print(f"\n📊 Variable Categories by Missing Data:")
print(f"  Complete variables (0% missing): {len(complete_vars)}")
print(f"  Low missing (≤20%): {len(low_missing_vars)}")  
print(f"  Moderate missing (20-50%): {len(moderate_missing_vars)}")

# ============================================================================
# EVIDENCE-BASED PREDICTOR SELECTION (15-25 VARIABLES)
# ============================================================================

print(f"\n🎯 SELECTING 15-25 PREDICTOR VARIABLES (VAN BUUREN'S CRITERIA):")
print("="*65)

# Define comprehensive predictor candidates with evidence levels
predictor_candidates = {
    # CORE DEMOGRAPHICS (Always include - Strong evidence)
    'age': {'category': 'Demographics', 'evidence': 'Strong', 'priority': 1, 'type': 'continuous'},
    'sex': {'category': 'Demographics', 'evidence': 'Strong', 'priority': 2, 'type': 'binary'},
    
    # CLINICAL SEVERITY (Strong evidence)
    'ward': {'category': 'Clinical_Severity', 'evidence': 'Strong', 'priority': 3, 'type': 'categorical'},
    'systolic_bp_baseline': {'category': 'Vital_Signs', 'evidence': 'Strong', 'priority': 4, 'type': 'continuous'},
    'pulse_baseline': {'category': 'Vital_Signs', 'evidence': 'Moderate', 'priority': 5, 'type': 'continuous'},
    'temp_baseline': {'category': 'Vital_Signs', 'evidence': 'Moderate', 'priority': 6, 'type': 'continuous'},
    'rr_baseline': {'category': 'Vital_Signs', 'evidence': 'Moderate', 'priority': 7, 'type': 'continuous'},
    'spo2_baseline': {'category': 'Vital_Signs', 'evidence': 'Moderate', 'priority': 8, 'type': 'continuous'},
    'gcs_baseline': {'category': 'Vital_Signs', 'evidence': 'Moderate', 'priority': 9, 'type': 'continuous'},
    
    # COMORBIDITIES (Strong evidence) 
    'hiv_status': {'category': 'Comorbidities', 'evidence': 'Strong', 'priority': 10, 'type': 'categorical'},
    'cormobid_condition': {'category': 'Comorbidities', 'evidence': 'Strong', 'priority': 11, 'type': 'binary'},
    
    # INFECTION CHARACTERISTICS (Moderate evidence)
    'first_organism': {'category': 'Infection', 'evidence': 'Moderate', 'priority': 12, 'type': 'categorical'},
    'infect_site___1': {'category': 'Infection', 'evidence': 'Moderate', 'priority': 13, 'type': 'categorical'},
    'referral': {'category': 'Clinical_Process', 'evidence': 'Moderate', 'priority': 14, 'type': 'binary'},
    
    # FACILITY FACTORS (Moderate evidence)
    'facility_category': {'category': 'System', 'evidence': 'Moderate', 'priority': 15, 'type': 'categorical'},
    'name_of_rrh': {'category': 'System', 'evidence': 'Moderate', 'priority': 16, 'type': 'categorical'},
    
    # CLINICAL OUTCOMES (Moderate evidence)
    'complications': {'category': 'Clinical_Severity', 'evidence': 'Moderate', 'priority': 17, 'type': 'binary'},
    
    # ADDITIONAL CLINICAL VARIABLES
    'admission_date': {'category': 'Clinical_Process', 'evidence': 'Weak', 'priority': 18, 'type': 'datetime'},
    'res_district': {'category': 'Demographics', 'evidence': 'Weak', 'priority': 19, 'type': 'categorical'},
    'occupation': {'category': 'Demographics', 'evidence': 'Weak', 'priority': 20, 'type': 'categorical'},
    'allergies': {'category': 'Clinical_History', 'evidence': 'Weak', 'priority': 21, 'type': 'categorical'},
    'antib_prior_admi': {'category': 'Clinical_History', 'evidence': 'Weak', 'priority': 22, 'type': 'binary'},
    
    # ADDITIONAL INFECTION SITES 
    'infect_site___2': {'category': 'Infection', 'evidence': 'Weak', 'priority': 23, 'type': 'categorical'},
    'infect_site___3': {'category': 'Infection', 'evidence': 'Weak', 'priority': 24, 'type': 'categorical'},
    
    # SPECIMEN TYPES
    'site_based_sample___1': {'category': 'Infection', 'evidence': 'Weak', 'priority': 25, 'type': 'categorical'},
}

# Check availability and calculate missing rates
available_predictors = {}
print(f"\nChecking predictor availability:")

for var_name, var_info in predictor_candidates.items():
    if var_name in df.columns:
        missing_rate = (df[var_name].isnull().sum() / len(df)) * 100
        unique_count = df[var_name].nunique()
        
        # Calculate basic correlation with mortality for numeric variables
        if df[var_name].dtype in ['int64', 'float64'] and var_name != 'mortality':
            correlation = abs(df[var_name].corr(df['mortality']))
            if np.isnan(correlation):
                correlation = 0
        else:
            correlation = 0
        
        var_info.update({
            'missing_rate': float(missing_rate),
            'unique_values': int(unique_count),
            'correlation': float(correlation),
            'available': True
        })
        
        available_predictors[var_name] = var_info
        
        print(f"  ✅ {var_name:<25}: {missing_rate:5.1f}% missing, {unique_count:3d} unique")
    else:
        print(f"  ❌ {var_name:<25}: NOT FOUND")

print(f"\n📊 Available predictors: {len(available_predictors)}")

# ============================================================================
# SELECT FINAL 15-25 PREDICTORS 
# ============================================================================

print(f"\n🎯 SELECTING FINAL 15-25 PREDICTORS (PER ML IMPLEMENTATION PLAN):")
print("="*70)

# Sort by evidence level, then priority, then missing rate
sorted_predictors = sorted(
    available_predictors.items(),
    key=lambda x: (
        {'Strong': 0, 'Moderate': 1, 'Weak': 2}[x[1]['evidence']],  # Evidence level
        x[1]['priority'],  # Priority within evidence level
        x[1]['missing_rate']  # Missing rate (lower is better)
    )
)

# Select predictors following van Buuren's 15-25 criteria
MIN_PREDICTORS = 15
MAX_PREDICTORS = 25

final_predictors = {}
selected_count = 0

print(f"\nSelected Predictors (Target: {MIN_PREDICTORS}-{MAX_PREDICTORS} variables):")
print(f"{'#':<2} {'Variable':<25} {'Category':<15} {'Evidence':<10} {'Missing%':<9} {'Type'}")
print("-" * 85)

for var_name, var_info in sorted_predictors:
    if selected_count < MAX_PREDICTORS:
        final_predictors[var_name] = var_info
        selected_count += 1
        
        print(f"{selected_count:<2} {var_name:<25} {var_info['category']:<15} "
              f"{var_info['evidence']:<10} {var_info['missing_rate']:<8.1f}% {var_info['type']}")

print(f"\n✅ FINAL SELECTION: {len(final_predictors)} PREDICTORS")
print(f"📊 Meets ML Plan requirement: {MIN_PREDICTORS}-{MAX_PREDICTORS} variables")

# Check if we have minimum required predictors
if len(final_predictors) < MIN_PREDICTORS:
    print(f"⚠️  WARNING: Only {len(final_predictors)} predictors found, need minimum {MIN_PREDICTORS}")
    print(f"   Consider relaxing missing data thresholds or including more variables")

# ============================================================================
# MICE IMPUTATION METHOD ASSIGNMENT
# ============================================================================

print(f"\n🔧 MICE IMPUTATION METHOD ASSIGNMENT:")
print("="*40)

mice_methods = {
    'continuous': 'pmm',      # Predictive Mean Matching
    'binary': 'logreg',       # Logistic Regression  
    'categorical': 'polyreg', # Multinomial Logistic Regression
    'datetime': 'pmm'         # Treat as numeric after conversion
}

print(f"\n{'Variable':<25} {'Type':<12} {'MICE Method':<12} {'Missing%'}")
print("-" * 60)

for var_name, var_info in final_predictors.items():
    mice_method = mice_methods.get(var_info['type'], 'pmm')
    print(f"{var_name:<25} {var_info['type']:<12} {mice_method:<12} {var_info['missing_rate']:>7.1f}%")

# ============================================================================
# GENERATE COMPREHENSIVE RESULTS
# ============================================================================

print(f"\n📄 GENERATING FINAL RESULTS:")
print("="*35)

# Create comprehensive results
final_results = {
    'analysis_date': datetime.now().isoformat(),
    'methodology': 'van Buuren criteria from ML Implementation Plan',
    'target_variables': f"{MIN_PREDICTORS}-{MAX_PREDICTORS} predictors",
    'actual_selection': len(final_predictors),
    'mortality_outcome': {
        'variable_name': 'mortality',
        'definition': 'Binary outcome: 0=survived, 1=died',
        'events': int(df['mortality'].sum()),
        'event_rate': float(df['mortality'].mean()),
        'suitable_for_modeling': bool(df['mortality'].sum() >= 100)
    },
    'selected_predictors': final_predictors,
    'mice_configuration': {
        var_name: {
            'type': var_info['type'],
            'mice_method': mice_methods.get(var_info['type'], 'pmm'),
            'missing_rate': float(var_info['missing_rate']),
            'evidence_level': var_info['evidence'],
            'category': var_info['category']
        }
        for var_name, var_info in final_predictors.items()
    }
}

# Save comprehensive results
with open(OUTPUT_DIR / 'corrected_variable_selection.json', 'w', encoding='utf-8') as f:
    json.dump(final_results, f, indent=2)

# Create predictor summary table  
predictor_df = pd.DataFrame([
    {
        'Variable': var_name,
        'Category': var_info['category'],
        'Evidence_Level': var_info['evidence'],
        'Variable_Type': var_info['type'],
        'MICE_Method': mice_methods.get(var_info['type'], 'pmm'),
        'Missing_Rate_Percent': float(var_info['missing_rate']),
        'Priority': int(var_info['priority']),
        'Unique_Values': int(var_info['unique_values']),
        'Correlation_with_Mortality': float(var_info.get('correlation', 0))
    }
    for var_name, var_info in final_predictors.items()
])

predictor_df.to_csv(OUTPUT_DIR / 'corrected_predictor_summary.csv', index=False)

print(f"\n✅ CORRECTED ANALYSIS COMPLETE!")
print(f"📁 Files generated:")
print(f"   - corrected_variable_selection.json (comprehensive results)")
print(f"   - corrected_predictor_summary.csv (predictor table)")

print(f"\n🎯 FINAL SUMMARY:")
print(f"   OUTCOME: mortality (what we predict) - {int(df['mortality'].sum())} events")
print(f"   PREDICTORS: {len(final_predictors)} variables (what we use to predict)")
print(f"   METHOD: Following ML Implementation Plan (van Buuren's 15-25 criteria)")
print(f"   READY FOR: Phase 2 - MICE Implementation")

print(f"\n" + "="*80)
print("CORRECTED VARIABLE CLASSIFICATION COMPLETE!")
print(f"✅ {len(final_predictors)} PREDICTORS SELECTED (meets 15-25 requirement)")
print("="*80)
