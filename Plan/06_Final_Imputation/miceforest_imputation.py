"""
Step 6: Final MICE Imputation using miceforest
Following ML Implementation Plan Steps 2.2-2.5

This implementation uses miceforest for proper:
- PMM (Predictive Mean Matching) for continuous variables
- LightGBM-based imputation with mean matching
- Proper handling of categorical variables
- Clinical bounds enforcement
"""
import json
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# Check for miceforest
try:
    import miceforest as mf
    print("✅ miceforest imported successfully")
except ImportError:
    print("❌ miceforest not installed. Please run: pip install miceforest")
    raise SystemExit(1)

# =============================================================================
# CONFIGURATION
# =============================================================================

PLAN_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan")
DATA_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025")
STEP3_DIR = PLAN_DIR / "03_Variable_Classification"
STEP4_DIR = PLAN_DIR / "04_MICE_Setup"
STEP6_DIR = PLAN_DIR / "06_Final_Imputation"

print("="*80)
print("STEP 6: FINAL MICE IMPUTATION WITH MICEFOREST")
print("Following ML Implementation Plan Steps 2.2-2.5")
print("="*80)

# Load configuration from previous steps
preds_df = pd.read_csv(STEP3_DIR / 'corrected_predictor_summary.csv')
sel = json.loads((STEP3_DIR / 'corrected_variable_selection.json').read_text(encoding='utf-8'))
mice_cfg = json.loads((STEP4_DIR / 'mice_config.json').read_text(encoding='utf-8'))

OUTCOME = sel['mortality_outcome']['variable_name']
ALL_PREDICTORS = preds_df['Variable'].tolist()
vtype = {r['Variable']: r['Variable_Type'] for _, r in preds_df.iterrows()}

# Imputation parameters - BATCH MODE
# Running in batches of 20 to avoid MemoryError
# Total target: 100 datasets (5 batches x 20)
BATCH_SIZE = 20
BATCH_NUMBER = 5  # Change this: 1, 2, 3, 4, or 5
ITERATIONS = 10
SEED = 42 + (BATCH_NUMBER - 1) * 100  # Different seed per batch for independence

# Calculate batch range
START_INDEX = (BATCH_NUMBER - 1) * BATCH_SIZE + 1  # 1, 21, 41, 61, 81
END_INDEX = BATCH_NUMBER * BATCH_SIZE  # 20, 40, 60, 80, 100
M_FINAL = BATCH_SIZE  # Datasets per batch

print(f"\n" + "="*60)
print(f"BATCH MODE: Batch {BATCH_NUMBER} of 5")
print(f"Creating datasets {START_INDEX} to {END_INDEX}")
print(f"="*60)

print(f"\nConfiguration:")
print(f"  - Final imputations (m): {M_FINAL}")
print(f"  - Iterations: {ITERATIONS}")
print(f"  - Outcome: {OUTCOME}")

# =============================================================================
# DATA LOADING AND PREPARATION
# =============================================================================

excel_path = DATA_DIR / "GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx"
df = pd.read_excel(excel_path, sheet_name=0)

# Create mortality outcome if needed
if OUTCOME not in df.columns:
    if 'treatment_outcome' not in df.columns:
        raise RuntimeError("treatment_outcome not found; cannot define mortality outcome")
    df[OUTCOME] = (df['treatment_outcome'] == 'Died').astype(int)

available = [c for c in ALL_PREDICTORS if c in df.columns]
print(f"\nData loaded: {df.shape[0]} patients, {len(available)} predictors available")

# Working dataframe: outcome + predictors
cols = [OUTCOME] + available
X = df[cols].copy()

# =============================================================================
# DATA PREPROCESSING
# =============================================================================

def parse_gcs(val):
    """Parse GCS values including E#V#M# format"""
    if pd.isna(val):
        return np.nan
    try:
        f = float(str(val))
        if np.isfinite(f):
            return float(np.clip(f, 3, 15))
    except:
        pass
    
    s = str(val).upper().replace(" ", "")
    m = re.findall(r"[EVM](\d+)", s)
    if m:
        try:
            total = sum(float(x) for x in m)
            return float(np.clip(total, 3, 15))
        except:
            return np.nan
    
    m2 = re.search(r"-?\d+(?:\.\d+)?", s)
    if m2:
        try:
            return float(np.clip(float(m2.group(0)), 3, 15))
        except:
            return np.nan
    return np.nan

def parse_numeric(val):
    """Parse numeric values including ranges like '92-93'"""
    if pd.isna(val):
        return np.nan
    if isinstance(val, (int, float, np.number)):
        return float(val)
    s = str(val).strip()
    if not s:
        return np.nan
    
    # Handle ranges
    m = re.match(r"^\s*(-?\d+(?:\.\d+)?)\s*[-–—]\s*(-?\d+(?:\.\d+)?)\s*$", s)
    if m:
        return (float(m.group(1)) + float(m.group(2))) / 2.0
    
    m2 = re.search(r"-?\d+(?:\.\d+)?", s)
    if m2:
        try:
            return float(m2.group(0))
        except:
            return np.nan
    return np.nan

# Apply GCS parsing
if 'gcs_baseline' in X.columns:
    X['gcs_baseline'] = X['gcs_baseline'].apply(parse_gcs)

# Convert datetime to numeric (days since epoch)
for c in available:
    if vtype.get(c) == 'datetime':
        try:
            X[c] = pd.to_datetime(X[c], errors='coerce')
            X[c] = (X[c] - pd.Timestamp('1970-01-01')) / pd.Timedelta(days=1)
        except:
            X[c] = pd.to_numeric(X[c], errors='coerce')

# Parse continuous variables
for c in available:
    if vtype.get(c) in ('continuous', 'datetime'):
        X[c] = X[c].apply(parse_numeric).astype(float)

# Identify variable types for miceforest
categorical_vars = [c for c in available if vtype.get(c) in ('categorical', 'binary')]
continuous_vars = [c for c in available if vtype.get(c) in ('continuous', 'datetime')]

print(f"\nVariable types:")
print(f"  - Continuous: {len(continuous_vars)}")
print(f"  - Categorical/Binary: {len(categorical_vars)}")

# Convert categorical to proper category dtype for miceforest
for c in categorical_vars:
    X[c] = X[c].astype('category')

# =============================================================================
# DATA CLEANING - Remove inf values (required by miceforest/scipy KDTree)
# =============================================================================

print(f"\nCleaning data (replacing inf with NaN)...")
n_inf_replaced = 0
for c in X.columns:
    if X[c].dtype in ['float64', 'float32', 'int64', 'int32']:
        inf_mask = np.isinf(X[c])
        n_inf = inf_mask.sum()
        if n_inf > 0:
            X.loc[inf_mask, c] = np.nan
            n_inf_replaced += n_inf
            print(f"  {c}: replaced {n_inf} inf values with NaN")

if n_inf_replaced == 0:
    print("  No inf values found - data is clean")
else:
    print(f"  Total: {n_inf_replaced} inf values replaced")

# Verify no inf values remain
for c in X.columns:
    if X[c].dtype in ['float64', 'float32']:
        assert not np.isinf(X[c]).any(), f"Inf values still present in {c}"

# =============================================================================
# CLINICAL BOUNDS DEFINITION
# =============================================================================

CLINICAL_BOUNDS = {
    'age': (0, 120, 'years'),
    'systolic_bp_baseline': (50, 250, 'mmHg'),
    'pulse_baseline': (20, 250, 'bpm'),
    'temp_baseline': (30, 43, '°C'),
    'rr_baseline': (5, 80, '/min'),
    'spo2_baseline': (50, 100, '%'),
    'gcs_baseline': (3, 15, 'points'),
    'admission_date': (12784, 22279, 'days')  # ~2005-2030
}

def enforce_clinical_bounds(df):
    """Enforce clinical bounds and count violations"""
    violations = {}
    for var, (lo, hi, unit) in CLINICAL_BOUNDS.items():
        if var in df.columns and df[var].dtype in ['float64', 'float32', 'int64', 'int32']:
            before = df[var].copy()
            df[var] = np.clip(df[var], lo, hi)
            n_violations = ((before < lo) | (before > hi)).sum()
            violations[var] = int(n_violations)
    return df, violations

# =============================================================================
# MICEFOREST IMPUTATION
# =============================================================================

print(f"\n{'='*80}")
print("RUNNING MICEFOREST IMPUTATION")
print(f"{'='*80}")

# Prepare data for miceforest (exclude outcome from imputation but include as predictor)
X_mice = X.copy()

# Create the imputation kernel
print(f"\nInitializing miceforest kernel...")
print(f"  - mean_match_candidates=5 (per ML Plan Step 2.2)")

# Build mean_match_strategy: "fast" for categorical/binary (avoids KDTree NaN issue)
# "normal" for continuous variables (uses proper PMM with KDTree)
mean_match_strategy = {}
for c in X_mice.columns:
    if c == OUTCOME:
        continue
    if vtype.get(c) in ('categorical', 'binary'):
        mean_match_strategy[c] = 'fast'  # Uses class probabilities, no KDTree
    else:
        mean_match_strategy[c] = 'normal'  # Uses PMM with KDTree

print(f"  - mean_match_strategy: 'fast' for {len(categorical_vars)} categorical vars")
print(f"  - mean_match_strategy: 'normal' for {len(continuous_vars)} continuous vars")

# miceforest v6.0+ API per official docs
# num_datasets creates multiple imputed datasets (not n_datasets in mice())
kernel = mf.ImputationKernel(
    data=X_mice,
    num_datasets=M_FINAL,  # Creates M_FINAL separate datasets
    random_state=SEED,
    mean_match_candidates=5,  # Donor pool size per ML Plan Step 2.2
    mean_match_strategy=mean_match_strategy,  # Fast for categorical, normal for continuous
)

# Run MICE iterations on all datasets
print(f"\nRunning MICE: {ITERATIONS} iterations on {M_FINAL} datasets...")
kernel.mice(iterations=ITERATIONS, verbose=True)

print(f"\n✅ MICE imputation completed")
print(f"  Datasets created: {M_FINAL}")

# Use M_FINAL as the actual count
n_datasets_created = M_FINAL

# =============================================================================
# CONVERGENCE DIAGNOSTICS
# =============================================================================

print(f"\n{'='*80}")
print("CONVERGENCE DIAGNOSTICS")
print(f"{'='*80}")

# Create diagnostics directory
diag_dir = STEP6_DIR / 'diagnostics'
diag_dir.mkdir(exist_ok=True)

# 1. Feature Importance - which variables predict missing values (per official docs)
print("\nGenerating diagnostic plots...")
try:
    # API: kernel.plot_feature_importance(dataset=0) - returns ggplot object
    fig = kernel.plot_feature_importance(dataset=0)
    if fig is not None:
        # plotnine ggplot objects use .save(), not .savefig()
        fig.save(diag_dir / 'feature_importance.png', dpi=150)
        print(f"  ✅ Saved: diagnostics/feature_importance.png")
    else:
        print(f"  ⚠️ Feature importance: No figure returned")
except Exception as e:
    print(f"  ⚠️ Feature importance plot failed: {e}")

# 2. Imputed Distributions - requires plotnine library
try:
    import plotnine  # Check if plotnine is installed
    fig = kernel.plot_imputed_distributions()
    if fig is not None:
        fig.save(diag_dir / 'imputed_distributions.png', dpi=150)
        print(f"  ✅ Saved: diagnostics/imputed_distributions.png")
except ImportError:
    print(f"  ⚠️ Imputed distributions: Skipped (requires 'pip install plotnine')")
except Exception as e:
    print(f"  ⚠️ Imputed distributions plot failed: {e}")

print("\n📊 CONVERGENCE BEST PRACTICES:")
print("   - Mean values should STABILIZE (flatten) after a few iterations")
print("   - If lines still trending up/down at final iteration → need more iterations")
print("   - Imputed distributions should roughly match observed distributions")
print("   - Typical: 5-20 iterations sufficient; rarely need >20")

# =============================================================================
# EXTRACT AND VALIDATE DATASETS
# =============================================================================

print(f"\n{'='*80}")
print("EXTRACTING AND VALIDATING DATASETS")
print(f"{'='*80}")

imputed_datasets = []
all_violations = {}
outcome_preserved = True

# Use actual number of datasets created
for i in range(n_datasets_created):
    # Extract completed dataset
    completed = kernel.complete_data(dataset=i)
    
    # Enforce clinical bounds
    completed, violations = enforce_clinical_bounds(completed)
    
    # Track violations
    for var, count in violations.items():
        if var not in all_violations:
            all_violations[var] = 0
        all_violations[var] += count
    
    # Verify outcome unchanged
    if not np.array_equal(completed[OUTCOME].values, X[OUTCOME].values):
        outcome_preserved = False
        # Restore outcome
        completed[OUTCOME] = X[OUTCOME].values
    
    imputed_datasets.append(completed)
    
    if (i + 1) % 20 == 0:
        print(f"  Processed {i + 1}/{n_datasets_created} datasets")

print(f"\n✅ Extracted {len(imputed_datasets)} datasets")
print(f"  - Outcome preserved: {'✅ Yes' if outcome_preserved else '⚠️ Restored'}")

# =============================================================================
# CLINICAL VALIDATION SUMMARY
# =============================================================================

print(f"\n{'='*80}")
print("CLINICAL VALIDATION RESULTS")
print(f"{'='*80}")

print(f"\nClinical Bounds Violations (per ML Plan Step 2.5):")
total_violations = 0
validation_results = {}

for var, (lo, hi, unit) in CLINICAL_BOUNDS.items():
    if var in X.columns and X[var].isnull().any():
        n_missing = X[var].isnull().sum()
        total_imputed = n_missing * n_datasets_created
        n_violations = all_violations.get(var, 0)
        violation_rate = n_violations / total_imputed if total_imputed > 0 else 0
        total_violations += n_violations
        
        if violation_rate == 0:
            status = "✅ EXCELLENT"
        elif violation_rate < 0.01:
            status = "⚠️ ACCEPTABLE"
        else:
            status = "❌ HIGH"
        
        validation_results[var] = {
            'bounds': f"{lo}-{hi} {unit}",
            'imputed_cells': total_imputed,
            'violations': n_violations,
            'violation_rate': violation_rate,
            'status': status
        }
        
        print(f"  {var:<25}: {violation_rate:6.2%} violations ({n_violations:,}/{total_imputed:,}) {status}")

# =============================================================================
# VERIFY SAMPLE DATA QUALITY
# =============================================================================

print(f"\n{'='*80}")
print("SAMPLE DATA QUALITY CHECK")
print(f"{'='*80}")

sample_df = imputed_datasets[0]
print(f"\nSample dataset 1 value ranges:")

for var, (lo, hi, unit) in CLINICAL_BOUNDS.items():
    if var in sample_df.columns:
        vmin, vmax = sample_df[var].min(), sample_df[var].max()
        in_bounds = lo <= vmin and vmax <= hi
        status = "✅" if in_bounds else "❌"
        print(f"  {var:<25}: {vmin:.2f} - {vmax:.2f} (bounds: {lo}-{hi}) {status}")

# Check categorical variables
print(f"\nCategorical variable check:")
for var in categorical_vars[:5]:  # Check first 5
    if var in sample_df.columns:
        unique_vals = sample_df[var].dropna().unique()
        n_unique = len(unique_vals)
        sample_vals = list(unique_vals[:5])
        print(f"  {var:<25}: {n_unique} unique values, sample: {sample_vals}")

# =============================================================================
# SAVE OUTPUTS
# =============================================================================

print(f"\n{'='*80}")
print("SAVING OUTPUTS")
print(f"{'='*80}")

# Create imputed_data subfolder and save ALL datasets
imputed_data_dir = STEP6_DIR / 'imputed_data'
imputed_data_dir.mkdir(exist_ok=True)

print(f"\nSaving batch {BATCH_NUMBER} datasets ({START_INDEX}-{END_INDEX}) to imputed_data/...")
sample_paths = []
for i in range(n_datasets_created):
    dataset_num = START_INDEX + i  # Use batch-adjusted index
    p = imputed_data_dir / f'imputed_dataset_{dataset_num}.csv'
    imputed_datasets[i].to_csv(p, index=False)
    sample_paths.append(p.name)
    print(f"  Saved: imputed_data/{p.name}")

print(f"\n✅ All {n_datasets_created} datasets saved to imputed_data/")

# Calculate distribution statistics
distribution_stats = {}
for var in continuous_vars:
    if var in X.columns and X[var].isnull().any():
        means = [ds[var].mean() for ds in imputed_datasets]
        stds = [ds[var].std() for ds in imputed_datasets]
        distribution_stats[var] = {
            'mean_across_imputations': np.mean(means),
            'std_of_means': np.std(means),
            'mean_within_imputation_std': np.mean(stds)
        }

dist_df = pd.DataFrame(distribution_stats).T
dist_df.to_csv(STEP6_DIR / 'miceforest_distributions.csv')
print(f"  Saved: miceforest_distributions.csv")

# Save summary JSON
summary = {
    'analysis_date': datetime.now().isoformat(),
    'method': 'miceforest (LightGBM with PMM)',
    'mean_match_candidates': 5,
    'iterations': ITERATIONS,
    'final_m': n_datasets_created,
    'outcome': OUTCOME,
    'n_patients': len(X),
    'n_predictors': len(available),
    'n_continuous': len(continuous_vars),
    'n_categorical': len(categorical_vars),
    'clinical_bounds_enforced': True,
    'total_violations': total_violations,
    'validation_results': {k: {kk: str(vv) for kk, vv in v.items()} 
                          for k, v in validation_results.items()},
    'outcome_preserved': outcome_preserved,
    'samples_saved': sample_paths
}

(STEP6_DIR / 'miceforest_summary.json').write_text(
    json.dumps(summary, indent=2, default=str), encoding='utf-8'
)
print(f"  Saved: miceforest_summary.json")

# =============================================================================
# GENERATE REPORT
# =============================================================================

report_lines = [
    "# Step 6: Final MICE Imputation Report",
    "",
    f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
    f"**Status:** {'✅ COMPLETE' if total_violations == 0 else '⚠️ COMPLETE WITH NOTES'}",
    "",
    "## Method",
    f"- **Library**: miceforest (LightGBM with Predictive Mean Matching)",
    f"- **Mean Match Candidates**: 5 (per ML Plan Step 2.2)",
    f"- **Iterations**: {ITERATIONS}",
    f"- **Final Imputations**: m={n_datasets_created}",
    f"- **Clinical Bounds**: ✅ Enforced per ML Plan Step 2.5",
    "",
    "## Data Summary",
    f"- **Patients**: {len(X):,}",
    f"- **Predictors**: {len(available)}",
    f"- **Continuous Variables**: {len(continuous_vars)}",
    f"- **Categorical Variables**: {len(categorical_vars)}",
    f"- **Outcome**: `{OUTCOME}` (preserved, not imputed)",
    "",
    "## Clinical Validation Results",
    "| Variable | Bounds | Imputed Cells | Violations | Rate | Status |",
    "|----------|--------|---------------|------------|------|--------|",
]

for var, results in validation_results.items():
    report_lines.append(
        f"| `{var}` | {results['bounds']} | {results['imputed_cells']:,} | "
        f"{results['violations']:,} | {results['violation_rate']:.2%} | {results['status']} |"
    )

report_lines.extend([
    "",
    "## Quality Assessment",
    f"- **Total Violations**: {total_violations:,}",
    f"- **Outcome Preserved**: {'✅ Yes' if outcome_preserved else '⚠️ Restored'}",
    f"- **Datasets Generated**: {n_datasets_created} complete multiply imputed datasets",
    "",
    "## Outputs",
    f"- `miceforest_summary.json` - Complete summary with validation",
    f"- `miceforest_distributions.csv` - Distribution statistics",
    f"- `miceforest_sample_*.csv` - Sample datasets for inspection",
    "",
    "## Next Steps",
    "- ✅ **Ready for Model Development**: Proceed to Phase 3",
    "- **Internal Validation**: Bootstrap with multiply imputed datasets",
    "- **Model Training**: Logistic regression / ML models with Rubin's rules",
])

(STEP6_DIR / 'miceforest_report.md').write_text('\n'.join(report_lines), encoding='utf-8')
print(f"  Saved: miceforest_report.md")

# =============================================================================
# FINAL STATUS
# =============================================================================

print(f"\n{'='*80}")
print("STEP 6 COMPLETE")
print(f"{'='*80}")
print(f"\n🎯 STATUS: READY FOR MODEL DEVELOPMENT")
print(f"   Method: miceforest with PMM")
print(f"   Datasets: {n_datasets_created} complete multiply imputed datasets")
print(f"   Clinical bounds: {'✅ ALL VALID' if total_violations == 0 else f'⚠️ {total_violations:,} violations (clipped)'}")
print(f"   Categorical handling: ✅ Proper (native miceforest support)")
print(f"\n   Next: Proceed to Phase 3 (Model Development)")
print("="*80)
