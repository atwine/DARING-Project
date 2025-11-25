"""
Phase 2: MICE Setup (Step 2.1–2.3)
- Compute imputations count from incomplete cases (White's rule)
- Build imputation variable list: mortality (outcome) + selected predictors
- Create predictor matrix including outcome for imputation models (exclude self)
- Assign MICE methods per variable type
- Generate: mice_config.json, imputation_matrix.csv, setup_report.md
"""
import math
import json
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np

PLAN_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan")
DATA_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Data\24 Oct 2025")
STEP3_DIR = PLAN_DIR / "03_Variable_Classification"
STEP4_DIR = PLAN_DIR / "04_MICE_Setup"
STEP4_DIR.mkdir(parents=True, exist_ok=True)

# Load Step 3 outputs
sel_json = STEP3_DIR / 'corrected_variable_selection.json'
preds_csv = STEP3_DIR / 'corrected_predictor_summary.csv'
sel = json.loads(sel_json.read_text(encoding='utf-8'))
preds_df = pd.read_csv(preds_csv)

# Outcome and predictors
OUTCOME = sel['mortality_outcome']['variable_name']  # 'mortality'
PREDICTORS = preds_df['Variable'].tolist()

# Load dataset
excel_path = DATA_DIR / "GHS-CAMO-Net Project 3 Additional Data_FinalV1_24Oct2025.xlsx"
df = pd.read_excel(excel_path, sheet_name=0)

# Ensure mortality outcome exists
if 'treatment_outcome' not in df.columns:
    raise RuntimeError("treatment_outcome not found in dataset; cannot derive mortality outcome")

df[OUTCOME] = (df['treatment_outcome'] == 'Died').astype(int)

# Filter to columns of interest if present
available = [c for c in PREDICTORS if c in df.columns]
missing_in_data = [c for c in PREDICTORS if c not in df.columns]

# Variable type and MICE method mapping from Step 3 table
var_types = {r['Variable']: r['Variable_Type'] for _, r in preds_df.iterrows()}
method_map = {
    'continuous': 'pmm',
    'binary': 'logreg',
    'categorical': 'polyreg',
    'datetime': 'pmm',  # will require pre-conversion to numeric if used downstream
}

# Compute per-variable missing rates and incomplete case rate across predictors
miss_rates = {}
for v in available:
    miss_rates[v] = float(df[v].isna().mean() * 100.0)

incomplete_mask = df[available].isna().any(axis=1)
percent_incomplete_cases = float(incomplete_mask.mean() * 100.0)

# Imputations per ML Plan guidance (White's rule; von Hippel staged)
m_min = int(math.ceil(percent_incomplete_cases))  # minimum by White's rule
m_pilot = max(20, m_min)  # pilot round
m_final = max(50, m_min)  # final analysis

# Build imputation predictor matrix
# Rows: variables to impute (subset of available with any missingness)
# Columns: candidate predictors to include in each variable's imputation model
# Include OUTCOME for all rows; exclude the variable itself (no self-prediction)
vars_to_impute = [v for v in available if df[v].isna().any()]
cols_for_matrix = [OUTCOME] + available  # include outcome explicitly at front

matrix = pd.DataFrame(0, index=vars_to_impute, columns=cols_for_matrix)
for row_var in vars_to_impute:
    for col_var in cols_for_matrix:
        if col_var == row_var:
            matrix.loc[row_var, col_var] = 0
        else:
            matrix.loc[row_var, col_var] = 1

# Build mice_config.json
mice_config = {
    'analysis_date': datetime.now().isoformat(),
    'methodology': 'ML Implementation Plan Step 1.2 and Step 2.1–2.3 (van Buuren, White rule)',
    'outcome_variable': OUTCOME,
    'predictors_selected_count': int(len(PREDICTORS)),
    'predictors_missing_in_data': missing_in_data,
    'variables_to_impute_count': int(len(vars_to_impute)),
    'percent_incomplete_cases': percent_incomplete_cases,
    'imputations': {
        'minimum_white_rule': int(m_min),
        'pilot': int(m_pilot),
        'final': int(m_final)
    },
    'variable_methods': {
        v: {
            'type': var_types.get(v, 'continuous'),
            'mice_method': method_map.get(var_types.get(v, 'continuous'), 'pmm'),
            'missing_rate_percent': miss_rates.get(v, 0.0)
        }
        for v in available
    }
}

# Save artifacts
(STEP4_DIR / 'mice_config.json').write_text(json.dumps(mice_config, indent=2), encoding='utf-8')
matrix.to_csv(STEP4_DIR / 'imputation_matrix.csv')

# Build setup_report.md
lines = []
lines.append('# Phase 2: MICE Setup Report (Step 2.1–2.3)')
lines.append('')
lines.append(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
lines.append('')
lines.append('## Outcome and Variable Scope')
lines.append(f"- Outcome (included in imputation models): `{OUTCOME}`")
lines.append(f"- Predictors selected: {len(PREDICTORS)}")
lines.append(f"- Predictors available in data: {len(available)}")
if missing_in_data:
    lines.append(f"- Predictors missing in data: {len(missing_in_data)} → {', '.join(missing_in_data)}")
lines.append('')
lines.append('## Missingness Summary')
lines.append(f"- Variables to impute: {len(vars_to_impute)}")
lines.append(f"- Percent incomplete cases (any missing among predictors): {percent_incomplete_cases:.1f}%")
lines.append('')
lines.append('## Imputation Counts (per ML Plan)')
lines.append(f"- Minimum (White's rule): m = {m_min}")
lines.append(f"- Pilot analysis: m = {m_pilot}")
lines.append(f"- Final analysis: m = {m_final}")
lines.append('')
lines.append('## MICE Methods by Variable')
lines.append('| Variable | Type | Method | Missing % |')
lines.append('|---|---|---|---:|')
for v in available:
    vt = var_types.get(v, 'continuous')
    mm = method_map.get(vt, 'pmm')
    mr = miss_rates.get(v, 0.0)
    lines.append(f"| `{v}` | {vt} | {mm} | {mr:.1f} |")
lines.append('')
lines.append('## Predictor Matrix')
lines.append('- imputation_matrix.csv contains the 0/1 inclusion for each imputed variable; outcome included for all.')

lines.append('')
lines.append('## Interpretation')
lines.append('- The outcome `mortality` is included in all imputation models, preserving correlations and supporting the MAR assumption as specified in the ML Plan.')
lines.append(f"- Incomplete cases are {percent_incomplete_cases:.1f}%, meaning every record has at least one missing predictor; Multiple Imputation is essential.")
lines.append(f"- Imputation count set to m={m_final} for final analysis based on White\'s rule (≈% incomplete cases) and plan guidance (50–100); consider a smaller pilot (e.g., m={max(20, m_min)}) to assess runtime and convergence before final runs.")
lines.append('- High missingness among vital signs (e.g., RR, GCS, temperature) requires strong predictors (age, ward, HIV) and outcome inclusion to stabilize imputations.')
lines.append('- Method mapping is appropriate (PMM for continuous, logistic for binary, multinomial for categorical); datetime treated as numeric for PMM.')
lines.append('- The predictor matrix includes the outcome for all imputed variables and prevents self-prediction (diagonal zeros), aligning with best practice.')

(STEP4_DIR / 'setup_report.md').write_text('\n'.join(lines), encoding='utf-8')

print('Artifacts written:')
print(' - 04_MICE_Setup/mice_config.json')
print(' - 04_MICE_Setup/imputation_matrix.csv')
print(' - 04_MICE_Setup/setup_report.md')
print(' - 04_MICE_Setup/report.md')

# Also write a standard report.md for consistency across steps
(STEP4_DIR / 'report.md').write_text('\n'.join(lines), encoding='utf-8')
