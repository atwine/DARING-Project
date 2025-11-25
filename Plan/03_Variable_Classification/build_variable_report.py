"""
Builds report.md for Step 3 summarizing outcome and selected predictors with justifications.
"""
import json
import pandas as pd
from pathlib import Path
from datetime import datetime

STEP_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\03_Variable_Classification")
sel_json = STEP_DIR / 'corrected_variable_selection.json'
summary_csv = STEP_DIR / 'corrected_predictor_summary.csv'
report_md = STEP_DIR / 'report.md'

# Load data
with open(sel_json, 'r', encoding='utf-8') as f:
    sel = json.load(f)

pred_df = pd.read_csv(summary_csv)

just_map = {
    'age': 'Age is a consistently strong predictor of mortality across infections.',
    'sex': 'Sex differences affect immune response and health-seeking behavior.',
    'ward': 'Ward type proxies acuity and monitoring intensity (ICU vs general).',
    'systolic_bp_baseline': 'Hypotension is a key sepsis severity marker.',
    'pulse_baseline': 'Tachycardia reflects physiologic stress and infection severity.',
    'temp_baseline': 'Fever patterns correlate with systemic inflammatory response.',
    'rr_baseline': 'Tachypnea indicates respiratory compromise and sepsis.',
    'spo2_baseline': 'Hypoxemia associates with adverse outcomes.',
    'gcs_baseline': 'Neurologic depression signals critical illness risk.',
    'hiv_status': 'Immunosuppression increases risk of severe infection and death.',
    'cormobid_condition': 'Comorbidity burden increases mortality risk.',
    'first_organism': 'Pathogen virulence profiles differ in mortality risk.',
    'infect_site___1': 'Infection site (e.g., bloodstream) has distinct risk profiles.',
    'referral': 'Referral captures delayed presentation and higher severity.',
    'facility_category': 'System capacity and resources vary by facility level.',
    'name_of_rrh': 'Facility-specific effects (case-mix, protocols) influence outcomes.',
    'complications': 'Complications reflect disease severity and clinical deterioration.',
    'admission_date': 'Seasonality and system load can affect outcomes.',
    'res_district': 'Geography proxies access to care and socioeconomic context.',
    'occupation': 'Socioeconomic factors influence baseline risk.',
    'allergies': 'Clinical history marker; weak predictor, possible auxiliary utility.',
    'antib_prior_admi': 'Prior antibiotics affect resistance and outcomes.',
    'infect_site___2': 'Additional infection site information refines risk.',
    'infect_site___3': 'Additional infection site information refines risk.',
    'site_based_sample___1': 'Specimen type supports infection source classification.'
}

# Build report content
lines = []
lines.append('# Step 3 Report: Variable Classification and Selection')
lines.append('')
lines.append(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
lines.append('')
lines.append('## Outcome (Target)')
mo = sel['mortality_outcome']
lines.append(f"- Variable: `{mo['variable_name']}` (0=survived, 1=died)")
lines.append(f"- Events: {mo['events']} ({mo['event_rate']*100:.1f}%)")
lines.append(f"- Suitable for modeling: {'Yes' if mo['suitable_for_modeling'] else 'No'}")
lines.append('')
lines.append('## Selected Predictors (15–25 per ML Plan)')
lines.append(f"- Count: {sel['actual_selection']}")
lines.append('')
lines.append('| Variable | Category | Type | Missing % | Evidence | Justification |')
lines.append('|---|---|---|---:|---|---|')
for _, r in pred_df.iterrows():
    var = r['Variable']
    cat = r['Category']
    vtype = r['Variable_Type']
    miss = r['Missing_Rate_Percent']
    ev = r['Evidence_Level']
    just = just_map.get(var, f"Selected based on category {cat} and data availability.")
    lines.append(f"| `{var}` | {cat} | {vtype} | {miss:.1f} | {ev} | {just} |")

lines.append('')
lines.append('## Methodology')
lines.append('- Followed van Buuren criteria: 15–25 variables for imputation models (per ML Plan, Step 1.2).')
lines.append('- Outcome included in imputation models; predictors chosen by evidence, priority, and missingness.')
lines.append('')
lines.append('## Interpretation')
lines.append('- The outcome `mortality` is the target and therefore is not listed among predictors by design; it is, however, included as a predictor in imputation models to preserve associations (per ML Plan Step 1.2).')
lines.append('- The selection of 25 predictors meets the 15–25 guidance and balances evidence strength with data availability.')
lines.append('- High missingness in vital signs underscores the need for MICE; including outcome and clinically relevant variables helps satisfy the MAR assumption.')
lines.append('- Variable-type-specific MICE methods (PMM for continuous, logistic for binary, multinomial for categorical) support stable imputations.')
lines.append('- This configuration aligns with TRIPOD+AI reporting and prepares for Phase 2 imputation.')
lines.append('')
lines.append('## Next')
lines.append('- Proceed to Phase 2: MICE configuration using selected predictors and auxiliary variables.')

report_md.write_text('\n'.join(lines), encoding='utf-8')
print('report.md generated')
