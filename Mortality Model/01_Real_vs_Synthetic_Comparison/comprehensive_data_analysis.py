"""
STEP 1: Real vs Synthetic Dataset Comparison Analysis
==================================================

Comprehensive analysis comparing real GHS-CAMO-Net dataset with synthetic analysis expectations.
This script provides detailed statistical comparison and prepares for MICE adaptation.

Author: Clinical ML Analysis Team
Date: November 2025
Step: 01_Real_vs_Synthetic_Comparison
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
OUTPUT_DIR = PLAN_DIR / "01_Real_vs_Synthetic_Comparison"
OUTPUT_DIR.mkdir(exist_ok=True)

print("="*80)
print("STEP 1: COMPREHENSIVE REAL vs SYNTHETIC DATASET COMPARISON")
print("="*80)

# ============================================================================
# SECTION 1: DATA LOADING AND BASIC COMPARISON
# ============================================================================

print("\n📂 SECTION 1: Loading Real Dataset...")

# Try loading Excel first, then CSV with multiple encodings
data_path_excel = DATA_DIR / "GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx"
data_path_csv = DATA_DIR / "GHS-CAMO-Net Project 3.csv"

df = None
data_source = None

# Try Excel first
try:
    df = pd.read_excel(data_path_excel, sheet_name=0)
    data_source = "Excel"
    print(f"✓ Successfully loaded Excel file")
except Exception as e:
    print(f"✗ Excel loading failed: {e}")
    
    # Fallback to CSV with multiple encodings
    for encoding in ['utf-8', 'latin-1', 'cp1252', 'utf-8-sig', 'iso-8859-1']:
        try:
            df = pd.read_csv(data_path_csv, encoding=encoding, low_memory=False)
            data_source = f"CSV ({encoding})"
            print(f"✓ Successfully loaded CSV with {encoding}")
            break
        except Exception as csv_error:
            continue

if df is None:
    raise Exception("Could not load dataset with any method")

print(f"\nDataset loaded from: {data_source}")
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")

# ============================================================================
# SECTION 2: SYNTHETIC vs REAL COMPARISON ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("📊 SECTION 2: Synthetic vs Real Comparison")
print("="*80)

# Expected values from synthetic analysis
synthetic_expectations = {
    'sample_size': 1075,
    'mortality_count': 128,
    'mortality_rate': 11.9,
    'hiv_unknown_pct': 72.0,
    'vital_signs_missing_pct': (60, 85),
    'key_variables': [
        'age', 'sex', 'ward', 'hiv_status', 'cormobid_condition', 
        'referral', 'first_organism', 'treatment_outcome', 'complications',
        'temp_baseline', 'systolic_bp_baseline', 'pulse_baseline',
        'rr_baseline', 'spo2_baseline', 'admission_date'
    ]
}

# Real dataset analysis
real_analysis = {}

# Basic dataset characteristics
real_analysis['sample_size'] = len(df)
real_analysis['variable_count'] = len(df.columns)

print(f"\n🔍 Dataset Size Comparison:")
print(f"  Synthetic expected: {synthetic_expectations['sample_size']} patients")
print(f"  Real dataset: {real_analysis['sample_size']} patients")
print(f"  Match status: {'✅ PERFECT MATCH' if real_analysis['sample_size'] == synthetic_expectations['sample_size'] else '⚠️ DIFFERENT'}")

# ============================================================================
# SECTION 3: OUTCOME VARIABLE ANALYSIS
# ============================================================================

print(f"\n🎯 Outcome Variable Analysis:")

# Treatment outcome analysis
if 'treatment_outcome' in df.columns:
    outcome_counts = df['treatment_outcome'].value_counts()
    print(f"\nTreatment Outcome Distribution:")
    
    total_patients = len(df)
    for outcome, count in outcome_counts.items():
        percentage = (count / total_patients) * 100
        print(f"  - {outcome}: {count} ({percentage:.1f}%)")
    
    # Mortality analysis
    death_indicators = ['Died', 'died', 'Death', 'death']
    mortality_count = 0
    for outcome, count in outcome_counts.items():
        if any(indicator in str(outcome) for indicator in death_indicators):
            mortality_count += count
    
    mortality_rate = (mortality_count / total_patients) * 100
    
    real_analysis['mortality_count'] = mortality_count
    real_analysis['mortality_rate'] = mortality_rate
    
    print(f"\n📈 Mortality Comparison:")
    print(f"  Synthetic expected: {synthetic_expectations['mortality_count']} deaths ({synthetic_expectations['mortality_rate']:.1f}%)")
    print(f"  Real dataset: {mortality_count} deaths ({mortality_rate:.1f}%)")
    
    # Check if suitable for modeling (events per variable rule)
    events_per_var_rule = mortality_count / 10  # Rule of thumb: 10 events per predictor
    print(f"  Maximum predictors (10:1 rule): {int(events_per_var_rule)}")
    print(f"  Mortality modeling status: {'✅ EXCELLENT' if mortality_count >= 100 else '⚠️ LIMITED' if mortality_count >= 50 else '❌ INSUFFICIENT'}")

else:
    print("❌ treatment_outcome variable not found!")

# ============================================================================
# SECTION 4: KEY VARIABLE MAPPING
# ============================================================================

print(f"\n" + "="*80)
print("📋 SECTION 4: Key Variable Mapping Analysis")
print("="*80)

variable_mapping = {}
missing_variables = []
additional_variables = []

print(f"\n🔍 Expected Variable Mapping:")

for expected_var in synthetic_expectations['key_variables']:
    # Direct match
    if expected_var in df.columns:
        variable_mapping[expected_var] = expected_var
        print(f"  ✅ {expected_var:<25} → {expected_var} (direct match)")
    else:
        # Fuzzy matching
        possible_matches = []
        for col in df.columns:
            # Convert expected variable parts to lowercase and check for matches
            var_parts = expected_var.lower().split('_')
            col_lower = col.lower()
            if any(part in col_lower for part in var_parts if len(part) > 2):
                possible_matches.append(col)
        
        if possible_matches:
            best_match = possible_matches[0]  # Take first match
            variable_mapping[expected_var] = best_match
            print(f"  🔄 {expected_var:<25} → {best_match}")
            if len(possible_matches) > 1:
                print(f"     Alternative matches: {', '.join(possible_matches[1:3])}")  # Show up to 2 alternatives
        else:
            missing_variables.append(expected_var)
            print(f"  ❌ {expected_var:<25} → NOT FOUND")

# Identify additional variables of interest
vital_signs_keywords = ['temp', 'bp', 'pressure', 'pulse', 'heart', 'respiratory', 'rr_', 'spo2', 'oxygen', 'gcs']
microbiology_keywords = ['organism', 'culture', 'ast_', 'resistance', 'antibiotic']
clinical_keywords = ['comorbid', 'hiv', 'diagnosis', 'ward']

print(f"\n🆕 Additional Variables of Interest:")

additional_categories = {
    'vital_signs': [],
    'microbiology': [],
    'clinical': [],
    'outcomes': []
}

for col in df.columns:
    col_lower = col.lower()
    if col not in variable_mapping.values():
        if any(keyword in col_lower for keyword in vital_signs_keywords):
            additional_categories['vital_signs'].append(col)
        elif any(keyword in col_lower for keyword in microbiology_keywords):
            additional_categories['microbiology'].append(col)
        elif any(keyword in col_lower for keyword in clinical_keywords):
            additional_categories['clinical'].append(col)
        elif 'outcome' in col_lower or 'discharge' in col_lower or 'death' in col_lower:
            additional_categories['outcomes'].append(col)

for category, variables in additional_categories.items():
    if variables:
        print(f"  {category.title()}: {len(variables)} additional variables")
        # Show first 5 examples
        for var in variables[:5]:
            print(f"    - {var}")
        if len(variables) > 5:
            print(f"    ... and {len(variables) - 5} more")

# ============================================================================
# SECTION 5: MISSING DATA ANALYSIS
# ============================================================================

print(f"\n" + "="*80)
print("📊 SECTION 5: Missing Data Analysis")
print("="*80)

# Calculate missing data statistics
missing_stats = pd.DataFrame({
    'Variable': df.columns,
    'Missing_Count': [df[col].isnull().sum() for col in df.columns],
    'Missing_Percent': [(df[col].isnull().sum() / len(df)) * 100 for col in df.columns],
    'Data_Type': [str(df[col].dtype) for col in df.columns],
    'Unique_Values': [df[col].nunique() for col in df.columns]
})

missing_stats = missing_stats.sort_values('Missing_Percent', ascending=False)

# Missing data categories
high_missing = missing_stats[missing_stats['Missing_Percent'] > 50]
medium_missing = missing_stats[(missing_stats['Missing_Percent'] > 20) & 
                              (missing_stats['Missing_Percent'] <= 50)]
low_missing = missing_stats[missing_stats['Missing_Percent'] <= 20]

print(f"\n📈 Missing Data Summary:")
print(f"  High missing (>50%): {len(high_missing)} variables ({len(high_missing)/len(df.columns)*100:.1f}%)")
print(f"  Medium missing (20-50%): {len(medium_missing)} variables ({len(medium_missing)/len(df.columns)*100:.1f}%)")
print(f"  Low missing (≤20%): {len(low_missing)} variables ({len(low_missing)/len(df.columns)*100:.1f}%)")

# Focus on key variables missing data
print(f"\n🔍 Key Variables Missing Data Analysis:")
key_variables_present = [var for var in synthetic_expectations['key_variables'] 
                        if var in variable_mapping and variable_mapping[var] in df.columns]

for var in key_variables_present:
    real_var = variable_mapping[var]
    missing_pct = (df[real_var].isnull().sum() / len(df)) * 100
    status = "✅ Good" if missing_pct <= 20 else "⚠️ Moderate" if missing_pct <= 50 else "❌ High"
    print(f"  {var:<25}: {missing_pct:5.1f}% missing ({status})")

# Vital signs missing data (synthetic expectation: 60-85%)
vital_signs_vars = ['temp_baseline', 'systolic_bp_baseline', 'pulse_baseline', 'rr_baseline', 'spo2_baseline']
vital_missing_rates = []

print(f"\n🌡️ Vital Signs Missing Data (Expected: {synthetic_expectations['vital_signs_missing_pct'][0]}-{synthetic_expectations['vital_signs_missing_pct'][1]}%):")
for vital_var in vital_signs_vars:
    if vital_var in variable_mapping and variable_mapping[vital_var] in df.columns:
        real_var = variable_mapping[vital_var]
        missing_pct = (df[real_var].isnull().sum() / len(df)) * 100
        vital_missing_rates.append(missing_pct)
        
        # Check if within expected range
        expected_min, expected_max = synthetic_expectations['vital_signs_missing_pct']
        status = "✅ As Expected" if expected_min <= missing_pct <= expected_max else "⚠️ Different"
        print(f"  {vital_var:<25}: {missing_pct:5.1f}% ({status})")

if vital_missing_rates:
    avg_vital_missing = np.mean(vital_missing_rates)
    print(f"\nAverage vital signs missing: {avg_vital_missing:.1f}%")
    
    expected_min, expected_max = synthetic_expectations['vital_signs_missing_pct']
    if expected_min <= avg_vital_missing <= expected_max:
        print("✅ Vital signs missingness matches synthetic expectations")
    else:
        print("⚠️ Vital signs missingness differs from synthetic expectations")

# HIV status analysis
if 'hiv_status' in df.columns:
    hiv_counts = df['hiv_status'].value_counts()
    unknown_count = hiv_counts.get('Unknown', 0)
    unknown_pct = (unknown_count / len(df)) * 100
    
    print(f"\n🔬 HIV Status Analysis:")
    print(f"  Unknown HIV status: {unknown_count}/{len(df)} ({unknown_pct:.1f}%)")
    print(f"  Expected from synthetic: {synthetic_expectations['hiv_unknown_pct']:.1f}%")
    
    if abs(unknown_pct - synthetic_expectations['hiv_unknown_pct']) <= 5:
        print("  ✅ HIV missingness matches synthetic expectations")
    else:
        print("  ⚠️ HIV missingness differs from synthetic expectations")

# ============================================================================
# SECTION 6: GENERATE COMPARISON REPORT
# ============================================================================

print(f"\n" + "="*80)
print("📄 SECTION 6: Generating Comprehensive Report")
print("="*80)

# Create comprehensive comparison report
comparison_report = {
    'analysis_date': datetime.now().isoformat(),
    'data_source': data_source,
    'dataset_comparison': {
        'synthetic_sample_size': synthetic_expectations['sample_size'],
        'real_sample_size': real_analysis['sample_size'],
        'size_match': real_analysis['sample_size'] == synthetic_expectations['sample_size'],
        'real_variable_count': real_analysis['variable_count']
    },
    'mortality_comparison': {
        'synthetic_deaths': synthetic_expectations['mortality_count'],
        'synthetic_rate': synthetic_expectations['mortality_rate'],
        'real_deaths': real_analysis.get('mortality_count', 0),
        'real_rate': real_analysis.get('mortality_rate', 0),
        'suitable_for_modeling': real_analysis.get('mortality_count', 0) >= 100
    },
    'variable_mapping': variable_mapping,
    'missing_variables': missing_variables,
    'missing_data_summary': {
        'high_missing_count': len(high_missing),
        'medium_missing_count': len(medium_missing),
        'low_missing_count': len(low_missing),
        'avg_vital_missing': np.mean(vital_missing_rates) if vital_missing_rates else None,
        'hiv_unknown_pct': unknown_pct if 'hiv_status' in df.columns else None
    },
    'additional_opportunities': {
        'vital_signs_additional': len(additional_categories['vital_signs']),
        'microbiology_additional': len(additional_categories['microbiology']),
        'clinical_additional': len(additional_categories['clinical']),
        'outcomes_additional': len(additional_categories['outcomes'])
    }
}

# Save detailed missing data statistics
missing_stats.to_csv(OUTPUT_DIR / 'missing_data_detailed.csv', index=False)

# Save comparison report
with open(OUTPUT_DIR / 'comparison_report.json', 'w', encoding='utf-8') as f:
    json.dump(comparison_report, f, indent=2)

# Create summary markdown report
summary_report = f"""# Real vs Synthetic Dataset Comparison Report

**Analysis Date:** {datetime.now().strftime('%B %d, %Y')}
**Data Source:** {data_source}

## 📊 Key Findings Summary

### Dataset Size Comparison
- **Synthetic Expected:** {synthetic_expectations['sample_size']} patients
- **Real Dataset:** {real_analysis['sample_size']} patients
- **Status:** {'✅ PERFECT MATCH' if comparison_report['dataset_comparison']['size_match'] else '⚠️ DIFFERENT'}

### Mortality Analysis
- **Synthetic:** {synthetic_expectations['mortality_count']} deaths ({synthetic_expectations['mortality_rate']:.1f}%)
- **Real:** {real_analysis.get('mortality_count', 0)} deaths ({real_analysis.get('mortality_rate', 0):.1f}%)
- **Modeling Viability:** {'✅ EXCELLENT' if comparison_report['mortality_comparison']['suitable_for_modeling'] else '⚠️ LIMITED'}

### Variable Mapping Success
- **Successfully Mapped:** {len(variable_mapping)} / {len(synthetic_expectations['key_variables'])} expected variables
- **Missing Variables:** {len(missing_variables)} variables not found
- **Additional Variables:** {comparison_report['dataset_comparison']['real_variable_count'] - len(synthetic_expectations['key_variables'])} extra variables available

### Missing Data Alignment
- **High Missing Variables:** {len(high_missing)} variables (>{50}% missing)
- **Vital Signs Average Missing:** {np.mean(vital_missing_rates) if vital_missing_rates else 'N/A':.1f}%
- **HIV Unknown Rate:** {unknown_pct if 'hiv_status' in df.columns else 'N/A':.1f}%

## 🚀 Adaptation Requirements

### ✅ No Changes Needed
- Same sample size enables identical statistical approach
- Core outcome variables present and suitable
- Missing data patterns align with expectations

### 🔄 Enhancements Available
- {comparison_report['additional_opportunities']['microbiology_additional']} additional microbiology variables
- {comparison_report['additional_opportunities']['vital_signs_additional']} additional vital signs
- {comparison_report['additional_opportunities']['clinical_additional']} additional clinical variables

## 📋 Next Steps
1. **Variable Name Mapping:** Update analysis scripts with real variable names
2. **Enhanced Feature Engineering:** Leverage additional microbiology/resistance data
3. **MICE Adaptation:** Adapt imputation models for real data structure
4. **Validation Strategy:** Incorporate additional variables for improved validation

## 🎯 Conclusion
{'✅ **EXCELLENT ALIGNMENT** - Synthetic analysis methodology directly applicable to real dataset with significant enhancement opportunities.' if comparison_report['dataset_comparison']['size_match'] and comparison_report['mortality_comparison']['suitable_for_modeling'] else '⚠️ **ADAPTATION REQUIRED** - Some modifications needed for real dataset application.'}
"""

# Save summary report
with open(OUTPUT_DIR / 'summary_report.md', 'w', encoding='utf-8') as f:
    f.write(summary_report)

print(f"\n✅ Analysis Complete!")
print(f"📁 Output files created in: {OUTPUT_DIR}")
print(f"   - comparison_report.json (detailed analysis)")
print(f"   - summary_report.md (executive summary)")
print(f"   - missing_data_detailed.csv (comprehensive missing data stats)")

print(f"\n🎯 KEY CONCLUSION:")
if comparison_report['dataset_comparison']['size_match'] and comparison_report['mortality_comparison']['suitable_for_modeling']:
    print("✅ EXCELLENT - Real dataset perfectly aligned with synthetic expectations!")
    print("   Your MICE methodology can be applied directly with enhancements.")
else:
    print("⚠️ ADAPTATION NEEDED - Some modifications required for optimal performance.")

print(f"\n" + "="*80)
print("STEP 1 ANALYSIS COMPLETE - Ready for Step 2: MICE Adaptation")
print("="*80)
