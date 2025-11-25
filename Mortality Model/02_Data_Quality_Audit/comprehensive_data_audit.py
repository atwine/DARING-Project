"""
PHASE 1, STEP 1.1: Comprehensive Data Quality Audit
===================================================

Following ML Implementation Plan for mortality prediction model.
Systematic missing data assessment to understand MCAR/MAR/MNAR patterns
and prepare for MICE implementation.

Focus: Mortality Prediction
Author: Clinical ML Analysis Team
Date: November 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set up paths
PLAN_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan")
DATA_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025")
OUTPUT_DIR = PLAN_DIR / "02_Data_Quality_Audit"
OUTPUT_DIR.mkdir(exist_ok=True)

print("="*80)
print("PHASE 1, STEP 1.1: COMPREHENSIVE DATA QUALITY AUDIT")
print("Focus: Mortality Prediction Model")
print("="*80)

# ============================================================================
# LOAD DATASET
# ============================================================================

print("\n📂 Loading Dataset...")
data_path_excel = DATA_DIR / "GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx"

try:
    df = pd.read_excel(data_path_excel, sheet_name=0)
    print(f"✓ Dataset loaded: {df.shape[0]} patients, {df.shape[1]} variables")
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# ============================================================================
# MORTALITY OUTCOME DEFINITION
# ============================================================================

print("\n🎯 MORTALITY OUTCOME ANALYSIS...")

# Define mortality outcome
if 'treatment_outcome' in df.columns:
    mortality_mapping = {'Died': 1}  # Primary mortality indicator
    df['mortality'] = df['treatment_outcome'].map(mortality_mapping).fillna(0)
    
    mortality_count = df['mortality'].sum()
    mortality_rate = (mortality_count / len(df)) * 100
    
    print(f"✓ Mortality outcome defined:")
    print(f"  - Deaths: {int(mortality_count)} ({mortality_rate:.1f}%)")
    print(f"  - Survivors: {int(len(df) - mortality_count)} ({100-mortality_rate:.1f}%)")
    print(f"  - Events per variable rule (10:1): Max {int(mortality_count/10)} predictors")
else:
    print("❌ treatment_outcome variable not found")
    exit()

# ============================================================================
# STEP 1.1A: COMPREHENSIVE MISSING DATA CALCULATION
# ============================================================================

print(f"\n" + "="*80)
print("STEP 1.1A: Missing Data Percentage Calculation")
print("="*80)

# Calculate missing data for all variables
missing_summary = pd.DataFrame({
    'Variable': df.columns,
    'Total_Count': len(df),
    'Missing_Count': [df[col].isnull().sum() for col in df.columns],
    'Present_Count': [df[col].notnull().sum() for col in df.columns],
    'Missing_Percent': [(df[col].isnull().sum() / len(df)) * 100 for col in df.columns],
    'Data_Type': [str(df[col].dtype) for col in df.columns],
    'Unique_Values': [df[col].nunique() for col in df.columns]
})

missing_summary = missing_summary.sort_values('Missing_Percent', ascending=False)

# Categorize missing data levels
extremely_high = missing_summary[missing_summary['Missing_Percent'] > 90]
very_high = missing_summary[(missing_summary['Missing_Percent'] > 50) & 
                            (missing_summary['Missing_Percent'] <= 90)]
moderate = missing_summary[(missing_summary['Missing_Percent'] > 20) & 
                          (missing_summary['Missing_Percent'] <= 50)]
low_missing = missing_summary[(missing_summary['Missing_Percent'] > 0) & 
                             (missing_summary['Missing_Percent'] <= 20)]
complete = missing_summary[missing_summary['Missing_Percent'] == 0]

print(f"\n📊 Missing Data Categories:")
print(f"  Extremely high (>90%): {len(extremely_high)} variables")
print(f"  Very high (50-90%): {len(very_high)} variables") 
print(f"  Moderate (20-50%): {len(moderate)} variables")
print(f"  Low (1-20%): {len(low_missing)} variables")
print(f"  Complete (0%): {len(complete)} variables")

# Save detailed missing data statistics
missing_summary.to_csv(OUTPUT_DIR / 'detailed_missing_analysis.csv', index=False)
print(f"✓ Detailed missing data saved to: detailed_missing_analysis.csv")

# ============================================================================
# STEP 1.1B: VITAL SIGNS SPECIFIC ANALYSIS
# ============================================================================

print(f"\n" + "="*80)
print("STEP 1.1B: Vital Signs Missingness Assessment")
print("="*80)

# Define vital signs variables based on our real data mapping
vital_signs = {
    'Temperature': 'temp_baseline',
    'Systolic BP': 'systolic_bp_baseline', 
    'Diastolic BP': 'diastolic_bp_baseline',
    'Pulse': 'pulse_baseline',
    'Respiratory Rate': 'rr_baseline',
    'Oxygen Saturation': 'spo2_baseline',
    'Glasgow Coma Scale': 'gcs_baseline'
}

vital_missing_rates = {}
print(f"\n🌡️ Baseline Vital Signs Missingness:")

for vital_name, vital_var in vital_signs.items():
    if vital_var in df.columns:
        missing_count = df[vital_var].isnull().sum()
        missing_pct = (missing_count / len(df)) * 100
        vital_missing_rates[vital_name] = missing_pct
        
        # Clinical interpretation
        if missing_pct > 80:
            status = "❌ Critical"
        elif missing_pct > 60:
            status = "⚠️ High" 
        elif missing_pct > 40:
            status = "⚠️ Moderate"
        else:
            status = "✅ Acceptable"
            
        print(f"  {vital_name:<20}: {missing_count:4d}/{len(df)} ({missing_pct:5.1f}%) {status}")
    else:
        print(f"  {vital_name:<20}: Variable not found")

if vital_missing_rates:
    avg_vital_missing = np.mean(list(vital_missing_rates.values()))
    print(f"\n📈 Vital Signs Summary:")
    print(f"  Average missingness: {avg_vital_missing:.1f}%")
    print(f"  Range: {min(vital_missing_rates.values()):.1f}% - {max(vital_missing_rates.values()):.1f}%")
    
    # Compare to implementation plan expectation (60-85%)
    if 60 <= avg_vital_missing <= 85:
        print(f"  ✅ Within expected range (60-85% from synthetic analysis)")
    else:
        print(f"  ⚠️ Outside expected range (60-85% from synthetic analysis)")

# ============================================================================
# STEP 1.1C: COMPLETE CASES ANALYSIS  
# ============================================================================

print(f"\n" + "="*80)
print("STEP 1.1C: Complete Cases Analysis")
print("="*80)

# Calculate complete cases for different variable sets

# All variables
complete_all = df.dropna().shape[0]
complete_all_pct = (complete_all / len(df)) * 100

print(f"\n📋 Complete Cases Analysis:")
print(f"  All {len(df.columns)} variables: {complete_all}/{len(df)} ({complete_all_pct:.1f}%)")

# Core mortality prediction variables (excluding high missing)
core_predictors = [
    'age', 'sex', 'ward', 'hiv_status', 'cormobid_condition',
    'referral', 'first_organism', 'complications'
]

# Add available vital signs with <80% missing
available_vitals = [var for name, var in vital_signs.items() 
                   if var in df.columns and var in vital_missing_rates 
                   and vital_missing_rates.get(name, 100) < 80]

mortality_predictors = core_predictors + available_vitals + ['treatment_outcome']

# Check which predictors exist in dataset
existing_predictors = [var for var in mortality_predictors if var in df.columns]
missing_predictors = [var for var in mortality_predictors if var not in df.columns]

if existing_predictors:
    complete_predictors = df[existing_predictors].dropna().shape[0]
    complete_predictors_pct = (complete_predictors / len(df)) * 100
    
    print(f"  Core predictors ({len(existing_predictors)} vars): {complete_predictors}/{len(df)} ({complete_predictors_pct:.1f}%)")
    print(f"    Variables included: {', '.join(existing_predictors[:5])}{'...' if len(existing_predictors) > 5 else ''}")

if missing_predictors:
    print(f"  ⚠️ Missing predictors: {', '.join(missing_predictors)}")

# Calculate missing data contribution by variable
print(f"\n🔍 Variables Contributing Most to Incompleteness:")
variable_impact = []
for var in existing_predictors:
    if var != 'treatment_outcome':  # Exclude outcome
        before_drop = len(df[existing_predictors].dropna())
        predictors_without_var = [v for v in existing_predictors if v != var]
        after_drop = len(df[predictors_without_var].dropna())
        impact = after_drop - before_drop
        
        variable_impact.append({
            'variable': var,
            'complete_cases_gained': impact,
            'missing_pct': (df[var].isnull().sum() / len(df)) * 100
        })

# Sort by impact
variable_impact = sorted(variable_impact, key=lambda x: x['complete_cases_gained'], reverse=True)

print("  Top 5 variables reducing complete cases:")
for i, var_info in enumerate(variable_impact[:5], 1):
    print(f"    {i}. {var_info['variable']:<20}: {var_info['complete_cases_gained']:4d} cases lost ({var_info['missing_pct']:5.1f}% missing)")

# ============================================================================
# STEP 1.1D: MISSING DATA PATTERN ANALYSIS
# ============================================================================

print(f"\n" + "="*80)
print("STEP 1.1D: Missing Data Pattern Analysis")
print("="*80)

# Analyze missing data patterns for mortality prediction
print(f"\n🔍 Missing Data Patterns by Mortality Status:")

# Compare missingness between survivors and deceased
for var in existing_predictors:
    if var != 'treatment_outcome' and var in df.columns:
        # Missing rates by mortality status
        died_missing = df[df['mortality'] == 1][var].isnull().mean() * 100
        survived_missing = df[df['mortality'] == 0][var].isnull().mean() * 100
        difference = died_missing - survived_missing
        
        # Statistical significance test would go here
        if abs(difference) > 10:  # >10% difference suggests pattern
            status = "⚠️ Pattern" if abs(difference) > 20 else "🔍 Notable"
            print(f"  {var:<25}: Died {died_missing:5.1f}% vs Survived {survived_missing:5.1f}% ({difference:+5.1f}%) {status}")

# Ward-based missing patterns
if 'ward' in df.columns:
    print(f"\n🏥 Missing Data Patterns by Ward:")
    ward_vital_missing = {}
    
    for ward in df['ward'].dropna().unique()[:5]:  # Top 5 wards
        ward_data = df[df['ward'] == ward]
        ward_count = len(ward_data)
        
        if ward_count >= 10:  # Only analyze wards with >=10 patients
            ward_avg_vital_missing = []
            for vital_name, vital_var in vital_signs.items():
                if vital_var in df.columns:
                    ward_missing = ward_data[vital_var].isnull().mean() * 100
                    ward_avg_vital_missing.append(ward_missing)
            
            if ward_avg_vital_missing:
                avg_missing = np.mean(ward_avg_vital_missing)
                ward_vital_missing[ward] = avg_missing
                print(f"  {ward:<20} (n={ward_count:3d}): {avg_missing:5.1f}% avg vital missing")

# ============================================================================
# STEP 1.1E: MISSING DATA MECHANISM ASSESSMENT
# ============================================================================

print(f"\n" + "="*80) 
print("STEP 1.1E: Missing Data Mechanism Assessment")
print("="*80)

print(f"\n🔬 Missing Data Mechanism Analysis:")

# Little's MCAR Test (conceptual - would need proper implementation)
print(f"  📊 Pattern-based Assessment:")

# Check for systematic patterns
systematic_patterns = 0
random_patterns = 0

# Analyze correlations between missingness indicators
vital_vars_present = [var for name, var in vital_signs.items() if var in df.columns]

if len(vital_vars_present) >= 2:
    # Create missingness indicators
    missingness_df = pd.DataFrame({
        var: df[var].isnull().astype(int) for var in vital_vars_present
    })
    
    # Calculate correlation between missingness patterns
    miss_corr = missingness_df.corr()
    
    # High correlations suggest systematic missingness
    high_corr_count = 0
    for i in range(len(miss_corr.columns)):
        for j in range(i+1, len(miss_corr.columns)):
            corr_val = miss_corr.iloc[i, j]
            if abs(corr_val) > 0.3:  # Moderate correlation threshold
                high_corr_count += 1
                print(f"    - {miss_corr.columns[i]} & {miss_corr.columns[j]}: r={corr_val:.3f}")
    
    if high_corr_count > 0:
        print(f"  ⚠️ Evidence of systematic missingness (MAR/MNAR likely)")
        mechanism_assessment = "MAR/MNAR"
    else:
        print(f"  ✅ Low correlation suggests MCAR possible")
        mechanism_assessment = "Possibly MCAR"
else:
    print(f"  ⚠️ Insufficient variables for correlation analysis")
    mechanism_assessment = "Unknown"

# ============================================================================
# GENERATE COMPREHENSIVE AUDIT REPORT
# ============================================================================

print(f"\n" + "="*80)
print("GENERATING COMPREHENSIVE AUDIT REPORT")
print("="*80)

# Compile audit results
audit_results = {
    'analysis_date': datetime.now().isoformat(),
    'dataset_summary': {
        'total_patients': len(df),
        'total_variables': len(df.columns),
        'mortality_events': int(mortality_count),
        'mortality_rate_pct': float(mortality_rate)
    },
    'missing_data_overview': {
        'extremely_high_missing': len(extremely_high),
        'very_high_missing': len(very_high),
        'moderate_missing': len(moderate),
        'low_missing': len(low_missing),
        'complete_variables': len(complete)
    },
    'vital_signs_analysis': vital_missing_rates,
    'complete_cases': {
        'all_variables': {'count': complete_all, 'percentage': float(complete_all_pct)},
        'core_predictors': {'count': complete_predictors, 'percentage': float(complete_predictors_pct)} if 'complete_predictors' in locals() else None
    },
    'missing_mechanism_assessment': mechanism_assessment,
    'recommendations': {
        'suitable_for_mice': True if mechanism_assessment in ['MAR/MNAR', 'Possibly MCAR'] else False,
        'max_predictors': int(mortality_count / 10),
        'high_missing_exclusion_candidates': extremely_high['Variable'].tolist()[:10]
    }
}

# Save audit results
with open(OUTPUT_DIR / 'comprehensive_audit_report.json', 'w', encoding='utf-8') as f:
    json.dump(audit_results, f, indent=2)

print(f"\n✅ Comprehensive Audit Complete!")
print(f"📁 Output files:")
print(f"  - comprehensive_audit_report.json (detailed results)")
print(f"  - detailed_missing_analysis.csv (all variables)")

print(f"\n🎯 KEY FINDINGS:")
print(f"  - Mortality events: {int(mortality_count)} (suitable for modeling)")
print(f"  - Complete cases: {complete_predictors_pct:.1f}% for core predictors") 
print(f"  - Vital signs missing: {avg_vital_missing:.1f}% average")
print(f"  - Missing mechanism: {mechanism_assessment}")
print(f"  - MICE suitable: {'✅ Yes' if audit_results['recommendations']['suitable_for_mice'] else '❌ No'}")

print(f"\n📋 NEXT STEPS:")
print(f"  1. Review missing data patterns and clinical interpretations")
print(f"  2. Select final predictor set for mortality model (<={int(mortality_count/10)} variables)")
print(f"  3. Proceed to Step 1.2: Variable Classification and Selection")

print(f"\n" + "="*80)
print("PHASE 1, STEP 1.1 COMPLETE!")
print("="*80)
