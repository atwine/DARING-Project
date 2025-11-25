"""
STARTER CODE: Clinical Outcomes Analysis
==========================================

This script helps you get started with analyzing your data for the research questions.
Run each section one at a time to understand your data better.

Author: Your Friendly Bioinformatics Assistant
Date: October 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Set display options for better readability
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 120)

print("="*80)
print("CLINICAL OUTCOMES ANALYSIS - STARTER CODE")
print("="*80)

# ============================================================================
# SECTION 1: LOAD AND BASIC EXPLORATION
# ============================================================================

print("\n📂 SECTION 1: Loading Data...")

# Load data
df = pd.read_csv('synthetic_output.csv', low_memory=False)

print(f"✓ Dataset loaded: {df.shape[0]} patients, {df.shape[1]} columns")

# Basic info
print("\nBasic Dataset Info:")
print(f"  - Total patients: {len(df)}")
print(f"  - Date range: {df['admission_date'].min()} to {df['admission_date'].max()}")
print(f"  - Hospitals: {df['name_of_rrh'].nunique()} unique facilities")

# ============================================================================
# SECTION 2: OUTCOME VARIABLE EXPLORATION (Focus on Question 1 - Mortality)
# ============================================================================

print("\n" + "="*80)
print("📊 SECTION 2: Exploring Outcome Variables")
print("="*80)

# Treatment outcomes
print("\n🎯 Treatment Outcomes Distribution:")
print(df['treatment_outcome'].value_counts())
print(f"\nMortality Rate: {(df['treatment_outcome']=='Died').sum() / len(df) * 100:.1f}%")

# Create binary mortality outcome
df['died'] = (df['treatment_outcome'] == 'Died').astype(int)

print(f"\n✓ Created binary outcome variable 'died':")
print(f"  - Died: {df['died'].sum()} ({df['died'].mean()*100:.1f}%)")
print(f"  - Survived: {(df['died']==0).sum()} ({(df['died']==0).mean()*100:.1f}%)")

# Complications
df['had_complications'] = (df['complications'] == 'Yes').astype(int)
print(f"\n✓ Complication Rate: {df['had_complications'].mean()*100:.1f}%")

# Self-discharge
df['self_discharged'] = (df['treatment_outcome'] == 'Self discharged').astype(int)
print(f"✓ Self-discharge Rate: {df['self_discharged'].mean()*100:.1f}%")

# ============================================================================
# SECTION 3: PREDICTOR VARIABLES - DEMOGRAPHICS
# ============================================================================

print("\n" + "="*80)
print("📊 SECTION 3: Exploring Predictor Variables - Demographics")
print("="*80)

# Age analysis
print("\n👤 AGE:")
print(f"  - Mean: {df['age'].mean():.1f} years")
print(f"  - Median: {df['age'].median():.1f} years")
print(f"  - Range: {df['age'].min():.0f} to {df['age'].max():.0f}")
print(f"  - Missing: {df['age'].isna().sum()}")

# Create age groups
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 40, 60, 100], 
                         labels=['Pediatric (<18)', 'Young Adult (18-40)', 
                                'Middle Age (40-60)', 'Elderly (60+)'])

print("\nAge Group Distribution:")
print(df['age_group'].value_counts())

# Mortality by age group
print("\nMortality Rate by Age Group:")
mortality_by_age = df.groupby('age_group')['died'].agg(['sum', 'mean', 'count'])
mortality_by_age.columns = ['Deaths', 'Mortality_Rate', 'Total']
mortality_by_age['Mortality_Rate'] = mortality_by_age['Mortality_Rate'] * 100
print(mortality_by_age)

# Sex
print("\n⚥ SEX:")
print(df['sex'].value_counts())
print("\nMortality by Sex:")
print(df.groupby('sex')['died'].agg(['sum', 'mean', 'count']))

# HIV Status
print("\n🧬 HIV STATUS:")
print(df['hiv_status'].value_counts())
print("\nMortality by HIV Status:")
hiv_mortality = df.groupby('hiv_status')['died'].agg(['sum', 'mean', 'count'])
hiv_mortality.columns = ['Deaths', 'Mortality_Rate', 'Total']
hiv_mortality['Mortality_Rate'] = hiv_mortality['Mortality_Rate'] * 100
print(hiv_mortality)

# ============================================================================
# SECTION 4: PREDICTOR VARIABLES - CLINICAL SEVERITY
# ============================================================================

print("\n" + "="*80)
print("📊 SECTION 4: Clinical Severity Indicators")
print("="*80)

# Ward type (proxy for severity)
print("\n🏥 WARD TYPE (Proxy for Severity):")
print(df['ward'].value_counts())

print("\nMortality by Ward Type:")
ward_mortality = df.groupby('ward')['died'].agg(['sum', 'mean', 'count'])
ward_mortality.columns = ['Deaths', 'Mortality_Rate', 'Total']
ward_mortality['Mortality_Rate'] = ward_mortality['Mortality_Rate'] * 100
ward_mortality = ward_mortality.sort_values('Mortality_Rate', ascending=False)
print(ward_mortality.head(10))

# Create ICU indicator (important severity marker)
df['is_icu'] = df['ward'].str.contains('ICU|HDU', case=False, na=False).astype(int)
print(f"\n✓ ICU/HDU patients: {df['is_icu'].sum()} ({df['is_icu'].mean()*100:.1f}%)")
print(f"✓ Mortality in ICU: {df[df['is_icu']==1]['died'].mean()*100:.1f}%")
print(f"✓ Mortality in non-ICU: {df[df['is_icu']==0]['died'].mean()*100:.1f}%")

# Comorbidities
print("\n🏥 COMORBIDITIES:")
print(df['cormobid_condition'].value_counts())

df['has_comorbidity'] = (df['cormobid_condition'] == 'Yes').astype(int)
print(f"\n✓ Patients with comorbidities: {df['has_comorbidity'].sum()} ({df['has_comorbidity'].mean()*100:.1f}%)")
print(f"✓ Mortality with comorbidities: {df[df['has_comorbidity']==1]['died'].mean()*100:.1f}%")
print(f"✓ Mortality without comorbidities: {df[df['has_comorbidity']==0]['died'].mean()*100:.1f}%")

# Referral status (patients transferred from other facilities often sicker)
df['was_referred'] = (df['referral'] == 'Yes').astype(int)
print(f"\n✓ Referred patients: {df['was_referred'].sum()} ({df['was_referred'].mean()*100:.1f}%)")
print(f"✓ Mortality in referred: {df[df['was_referred']==1]['died'].mean()*100:.1f}%")
print(f"✓ Mortality in non-referred: {df[df['was_referred']==0]['died'].mean()*100:.1f}%")

# ============================================================================
# SECTION 5: PREDICTOR VARIABLES - INFECTION CHARACTERISTICS
# ============================================================================

print("\n" + "="*80)
print("📊 SECTION 5: Infection Characteristics")
print("="*80)

# Organism
print("\n🦠 ORGANISMS ISOLATED:")
print(df['first_organism'].value_counts().head(10))

# Mortality by top organisms
print("\nMortality by Organism (Top 5):")
top_organisms = df['first_organism'].value_counts().head(5).index
for org in top_organisms:
    org_data = df[df['first_organism'] == org]
    mortality_rate = org_data['died'].mean() * 100
    count = len(org_data)
    deaths = org_data['died'].sum()
    print(f"  {org}: {mortality_rate:.1f}% ({deaths}/{count})")

# Specimen type
print("\n🧪 SPECIMEN TYPES:")
print(df['specimen_type'].value_counts().head(8))

# ============================================================================
# SECTION 6: MISSING DATA ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("📊 SECTION 6: Missing Data Assessment")
print("="*80)

# Key variables for mortality model
key_vars = ['age', 'sex', 'ward', 'hiv_status', 'cormobid_condition', 
            'referral', 'first_organism', 'treatment_outcome',
            'temp_baseline', 'systolic_bp_baseline', 'pulse_baseline']

print("\nMissing Data in Key Variables:")
missing_summary = pd.DataFrame({
    'Variable': key_vars,
    'Missing_Count': [df[var].isna().sum() for var in key_vars],
    'Missing_Percent': [df[var].isna().sum() / len(df) * 100 for var in key_vars]
})
missing_summary = missing_summary.sort_values('Missing_Percent', ascending=False)
print(missing_summary.to_string(index=False))

print("\n⚠️ HIGH MISSINGNESS ALERT:")
high_missing = missing_summary[missing_summary['Missing_Percent'] > 50]
if len(high_missing) > 0:
    print(f"Variables with >50% missing:")
    for _, row in high_missing.iterrows():
        print(f"  - {row['Variable']}: {row['Missing_Percent']:.1f}% missing")
else:
    print("  None - Good news!")

# ============================================================================
# SECTION 7: SIMPLE MORTALITY MODEL (Demonstration)
# ============================================================================

print("\n" + "="*80)
print("📊 SECTION 7: Simple Mortality Prediction Model (Demo)")
print("="*80)

# Prepare data for modeling
print("\n🔧 Preparing data for modeling...")

# Select features that have low missingness
model_df = df[['died', 'age', 'sex', 'is_icu', 'has_comorbidity', 
               'was_referred', 'first_organism']].copy()

# Handle missing values
model_df = model_df.dropna(subset=['died', 'age'])  # Need outcome and age

# Create dummy variables for categorical features
model_df = pd.get_dummies(model_df, columns=['sex', 'first_organism'], drop_first=True)

# Drop any remaining rows with missing values (simple approach)
model_df = model_df.dropna()

print(f"✓ Clean dataset for modeling: {len(model_df)} patients")
print(f"✓ Features available: {model_df.shape[1] - 1}")  # -1 for outcome variable
print(f"✓ Deaths in modeling dataset: {model_df['died'].sum()} ({model_df['died'].mean()*100:.1f}%)")

# Split data
X = model_df.drop('died', axis=1)
y = model_df['died']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
                                                      random_state=42, stratify=y)

print(f"\n✓ Training set: {len(X_train)} patients ({y_train.sum()} deaths)")
print(f"✓ Testing set: {len(X_test)} patients ({y_test.sum()} deaths)")

# Build simple logistic regression model
print("\n🤖 Building Logistic Regression Model...")
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred_proba = model.predict_proba(X_test)[:, 1]
y_pred = model.predict(X_test)

# Evaluate
auc_score = roc_auc_score(y_test, y_pred_proba)

print("\n" + "="*80)
print("📈 MODEL PERFORMANCE")
print("="*80)
print(f"\n🎯 AUC-ROC Score: {auc_score:.3f}")

if auc_score >= 0.80:
    print("   → EXCELLENT discrimination!")
elif auc_score >= 0.70:
    print("   → GOOD discrimination!")
elif auc_score >= 0.60:
    print("   → ACCEPTABLE discrimination")
else:
    print("   → POOR discrimination - needs improvement")

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Survived', 'Died']))

print("\n📊 Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"True Negatives (Correctly predicted survivors): {cm[0,0]}")
print(f"False Positives (Predicted death but survived): {cm[0,1]}")
print(f"False Negatives (Predicted survival but died): {cm[1,0]}")
print(f"True Positives (Correctly predicted deaths): {cm[1,1]}")

# Feature importance (coefficients)
print("\n📊 Feature Importance (Top 10):")
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
})
feature_importance['Abs_Coef'] = abs(feature_importance['Coefficient'])
feature_importance = feature_importance.sort_values('Abs_Coef', ascending=False)
print(feature_importance.head(10).to_string(index=False))

print("\n" + "="*80)
print("✅ ANALYSIS COMPLETE!")
print("="*80)

print("\n📝 KEY FINDINGS:")
print(f"1. You have {len(df)} patients with {df['died'].sum()} deaths ({df['died'].mean()*100:.1f}%)")
print(f"2. A simple model achieved AUC of {auc_score:.3f}")
print(f"3. Key risk factors identified (see feature importance above)")
print(f"4. Model uses variables available at admission (practical!)")

print("\n🚀 NEXT STEPS:")
print("1. Improve feature engineering (create more meaningful variables)")
print("2. Handle missing data more sophisticatedly (imputation)")
print("3. Try advanced models (Random Forest, XGBoost)")
print("4. Add vital signs if you can recover that data")
print("5. Cross-validate for more robust performance estimates")
print("6. Create risk categories (Low/Medium/High risk)")
print("7. Validate on different time periods or hospitals")

print("\n" + "="*80)
print("💡 This is just a starting point! You can build on this framework.")
print("="*80)
