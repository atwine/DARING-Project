"""
MICE Imputation Quality Evaluation
Comprehensive assessment of corrected MICE implementation per ML Plan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json
from scipy import stats

STEP5_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\05_MICE_Pilot_Imputation")
PLAN_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan")
DATA_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025")

print("="*80)
print("MICE IMPUTATION QUALITY EVALUATION")
print("Assessing corrected implementation per ML Plan Steps 2.2-2.5")
print("="*80)

# Load original data and configuration
excel_path = DATA_DIR / "GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx"
df_orig = pd.read_excel(excel_path, sheet_name=0)
df_orig['mortality'] = (df_orig['treatment_outcome'] == 'Died').astype(int)

# Load imputed samples
sample_files = list(STEP5_DIR.glob('corrected_mice_sample_*.csv'))
print(f"\nFound {len(sample_files)} imputed sample files")

if len(sample_files) == 0:
    print("❌ No imputed samples found. Run corrected_mice_imputation.py first.")
    exit()

# Load all available samples
imputed_samples = []
for i, file_path in enumerate(sorted(sample_files)):
    df_imp = pd.read_csv(file_path)
    imputed_samples.append(df_imp)
    print(f"  Sample {i+1}: {df_imp.shape[0]} rows, {df_imp.shape[1]} columns")

n_samples = len(imputed_samples)
if n_samples < 5:
    print(f"⚠️  Only {n_samples} samples available (recommended: ≥5 for robust evaluation)")

# ============================================================================
# 1. CLINICAL BOUNDS VALIDATION
# ============================================================================

print(f"\n" + "="*60)
print("1. CLINICAL BOUNDS VALIDATION")
print("="*60)

clinical_bounds = {
    'age': (0, 120, 'years'),
    'systolic_bp_baseline': (50, 250, 'mmHg'), 
    'pulse_baseline': (20, 250, 'bpm'),
    'temp_baseline': (30, 43, '°C'),
    'rr_baseline': (5, 80, '/min'),
    'spo2_baseline': (50, 100, '%'),
    'gcs_baseline': (3, 15, 'points')
}

bounds_results = {}
print(f"{'Variable':<25} {'Bounds':<15} {'Violations':<12} {'Rate':<8} {'Status'}")
print("-" * 70)

for var, (lo, hi, unit) in clinical_bounds.items():
    if var not in imputed_samples[0].columns:
        continue
        
    total_violations = 0
    total_values = 0
    
    for df_imp in imputed_samples:
        # Check only originally missing positions (approximate)
        miss_mask = df_orig[var].isna() if var in df_orig.columns else pd.Series(True, index=df_imp.index)
        vals_to_check = pd.to_numeric(df_imp.loc[miss_mask, var], errors='coerce').dropna()
        
        violations = ((vals_to_check < lo) | (vals_to_check > hi)).sum()
        total_violations += violations
        total_values += len(vals_to_check)
    
    violation_rate = total_violations / total_values if total_values > 0 else 0
    status = "✅ PASS" if violation_rate < 0.01 else ("⚠️  WARN" if violation_rate < 0.05 else "❌ FAIL")
    
    bounds_results[var] = {
        'bounds': f"{lo}-{hi} {unit}",
        'violations': total_violations,
        'total': total_values,
        'rate': violation_rate,
        'status': status
    }
    
    print(f"{var:<25} {bounds_results[var]['bounds']:<15} {total_violations:<12} {violation_rate:<7.1%} {status}")

# ============================================================================
# 2. DISTRIBUTIONAL SIMILARITY ANALYSIS
# ============================================================================

print(f"\n" + "="*60)
print("2. DISTRIBUTIONAL SIMILARITY (OBSERVED vs IMPUTED)")
print("="*60)

dist_results = {}
continuous_vars = ['age', 'systolic_bp_baseline', 'pulse_baseline', 'temp_baseline', 
                  'rr_baseline', 'spo2_baseline', 'gcs_baseline']

print(f"{'Variable':<25} {'KS Stat':<10} {'|SMD|':<8} {'n_obs':<8} {'n_imp':<8} {'Quality'}")
print("-" * 70)

for var in continuous_vars:
    if var not in imputed_samples[0].columns or var not in df_orig.columns:
        continue
        
    # Observed values (convert to numeric, filter out non-numeric)
    obs_vals = pd.to_numeric(df_orig[var].dropna(), errors='coerce').dropna()
    if len(obs_vals) < 10:
        continue
    
    # Collect imputed values from all samples (convert to numeric)
    all_imputed = []
    for df_imp in imputed_samples:
        miss_mask = df_orig[var].isna()
        imp_vals = pd.to_numeric(df_imp.loc[miss_mask, var], errors='coerce').dropna()
        all_imputed.extend(imp_vals.tolist())
    
    if len(all_imputed) == 0:
        continue
    
    # Calculate KS statistic and SMD (both arrays now guaranteed numeric)
    ks_stat, ks_p = stats.ks_2samp(obs_vals, all_imputed)
    
    obs_mean, obs_std = obs_vals.mean(), obs_vals.std()
    imp_mean, imp_std = np.mean(all_imputed), np.std(all_imputed)
    pooled_std = np.sqrt((obs_std**2 + imp_std**2) / 2)
    smd = abs(obs_mean - imp_mean) / pooled_std if pooled_std > 0 else 0
    
    # Quality assessment
    ks_good = ks_stat < 0.2
    smd_good = smd < 0.1
    quality = "✅ GOOD" if (ks_good and smd_good) else ("⚠️  FAIR" if (ks_good or smd_good) else "❌ POOR")
    
    dist_results[var] = {
        'ks_stat': ks_stat,
        'smd': smd,
        'n_obs': len(obs_vals),
        'n_imputed': len(all_imputed),
        'quality': quality
    }
    
    print(f"{var:<25} {ks_stat:<9.3f} {smd:<7.3f} {len(obs_vals):<8} {len(all_imputed):<8} {quality}")

# ============================================================================
# 3. BETWEEN-IMPUTATION VARIABILITY
# ============================================================================

print(f"\n" + "="*60)
print("3. BETWEEN-IMPUTATION VARIABILITY")
print("="*60)

variability_results = {}
print(f"{'Variable':<25} {'Mean_CV':<10} {'SD_CV':<10} {'Stability'}")
print("-" * 55)

for var in continuous_vars:
    if var not in imputed_samples[0].columns:
        continue
        
    # Calculate means and SDs across imputations
    means = [df_imp[var].mean() for df_imp in imputed_samples]
    sds = [df_imp[var].std() for df_imp in imputed_samples]
    
    # Coefficient of variation for means and SDs
    mean_cv = np.std(means) / np.mean(means) if np.mean(means) > 0 else 0
    sd_cv = np.std(sds) / np.mean(sds) if np.mean(sds) > 0 else 0
    
    # Stability assessment
    stable = mean_cv < 0.05 and sd_cv < 0.1
    stability = "✅ STABLE" if stable else ("⚠️  MODERATE" if mean_cv < 0.1 else "❌ UNSTABLE")
    
    variability_results[var] = {
        'mean_cv': mean_cv,
        'sd_cv': sd_cv,
        'stability': stability
    }
    
    print(f"{var:<25} {mean_cv:<9.3f} {sd_cv:<9.3f} {stability}")

# ============================================================================
# 4. OUTCOME PRESERVATION CHECK
# ============================================================================

print(f"\n" + "="*60)
print("4. OUTCOME PRESERVATION (MORTALITY)")
print("="*60)

mortality_checks = []
for i, df_imp in enumerate(imputed_samples):
    if 'mortality' in df_imp.columns and 'mortality' in df_orig.columns:
        # Check if mortality values are identical (should be unchanged)
        identical = (df_imp['mortality'] == df_orig['mortality']).all()
        deaths = df_imp['mortality'].sum()
        rate = deaths / len(df_imp)
        
        mortality_checks.append({
            'sample': i + 1,
            'identical': identical,
            'deaths': deaths,
            'rate': rate
        })
        
        status = "✅ PRESERVED" if identical else "❌ MODIFIED"
        print(f"Sample {i+1}: {deaths} deaths ({rate:.1%}) - {status}")

outcome_preserved = all(check['identical'] for check in mortality_checks)

# ============================================================================
# 5. OVERALL QUALITY ASSESSMENT
# ============================================================================

print(f"\n" + "="*80)
print("OVERALL QUALITY ASSESSMENT")
print("="*80)

# Count quality metrics
bounds_pass = sum(1 for r in bounds_results.values() if r['status'] == "✅ PASS")
bounds_total = len(bounds_results)

dist_good = sum(1 for r in dist_results.values() if r['quality'] == "✅ GOOD")
dist_total = len(dist_results)

var_stable = sum(1 for r in variability_results.values() if r['stability'] == "✅ STABLE")
var_total = len(variability_results)

# Overall scores
bounds_score = bounds_pass / bounds_total if bounds_total > 0 else 0
dist_score = dist_good / dist_total if dist_total > 0 else 0
var_score = var_stable / var_total if var_total > 0 else 0

overall_score = (bounds_score + dist_score + var_score) / 3

print(f"📊 Clinical Bounds Compliance: {bounds_pass}/{bounds_total} ({bounds_score:.1%})")
print(f"📊 Distributional Quality: {dist_good}/{dist_total} ({dist_score:.1%})")  
print(f"📊 Variability Stability: {var_stable}/{var_total} ({var_score:.1%})")
print(f"📊 Outcome Preservation: {'✅ YES' if outcome_preserved else '❌ NO'}")
print(f"📊 Number of Imputations: {n_samples} (recommended: ≥5)")

print(f"\n🎯 **OVERALL QUALITY SCORE: {overall_score:.1%}**")

if overall_score >= 0.8:
    quality_rating = "✅ EXCELLENT"
    recommendation = "Ready for final imputation (m=100)"
elif overall_score >= 0.6:
    quality_rating = "⚠️  GOOD"
    recommendation = "Minor improvements recommended before final imputation"
elif overall_score >= 0.4:
    quality_rating = "⚠️  FAIR" 
    recommendation = "Significant improvements needed"
else:
    quality_rating = "❌ POOR"
    recommendation = "Major revision required"

print(f"🏆 Quality Rating: {quality_rating}")
print(f"💡 Recommendation: {recommendation}")

# ============================================================================
# 6. SAVE EVALUATION REPORT
# ============================================================================

evaluation_summary = {
    'analysis_date': pd.Timestamp.now().isoformat(),
    'n_samples_evaluated': n_samples,
    'overall_score': overall_score,
    'quality_rating': quality_rating,
    'recommendation': recommendation,
    'bounds_compliance': bounds_score,
    'distributional_quality': dist_score,
    'variability_stability': var_score,
    'outcome_preserved': outcome_preserved,
    'detailed_results': {
        'bounds': bounds_results,
        'distributions': dist_results,
        'variability': variability_results
    }
}

# Save evaluation results
eval_file = STEP5_DIR / 'mice_evaluation_report.json'
with open(eval_file, 'w', encoding='utf-8') as f:
    json.dump(evaluation_summary, f, indent=2, default=str)

print(f"\n✅ Evaluation complete!")
print(f"📁 Results saved to: {eval_file.name}")
print("="*80)
