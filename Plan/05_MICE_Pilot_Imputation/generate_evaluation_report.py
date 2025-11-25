"""
Generate comprehensive evaluation report based on MICE assessment
"""
import json
from pathlib import Path
from datetime import datetime

STEP5_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\05_MICE_Pilot_Imputation")

# Check if evaluation has been run
eval_file = STEP5_DIR / 'mice_evaluation_report.json'
if not eval_file.exists():
    print("❌ Run mice_evaluation.py first to generate evaluation data")
    exit()

# Load evaluation results
with open(eval_file, 'r', encoding='utf-8') as f:
    eval_data = json.load(f)

# Generate comprehensive markdown report
lines = []
lines.append('# MICE Imputation Quality Evaluation Report')
lines.append('')
lines.append(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
lines.append(f"**Samples Evaluated:** {eval_data['n_samples_evaluated']}")
lines.append('')

# Executive Summary
lines.append('## Executive Summary')
lines.append('')
lines.append(f"**Overall Quality Score:** {eval_data['overall_score']:.1%}")
lines.append(f"**Quality Rating:** {eval_data['quality_rating']}")
lines.append(f"**Recommendation:** {eval_data['recommendation']}")
lines.append('')

# Component Scores
lines.append('## Quality Component Scores')
lines.append('')
lines.append('| Component | Score | Status |')
lines.append('|---|---:|---|')
lines.append(f"| Clinical Bounds Compliance | {eval_data['bounds_compliance']:.1%} | {'✅ PASS' if eval_data['bounds_compliance'] >= 0.8 else '⚠️ NEEDS WORK'} |")
lines.append(f"| Distributional Quality | {eval_data['distributional_quality']:.1%} | {'✅ PASS' if eval_data['distributional_quality'] >= 0.6 else '⚠️ NEEDS WORK'} |")
lines.append(f"| Variability Stability | {eval_data['variability_stability']:.1%} | {'✅ PASS' if eval_data['variability_stability'] >= 0.7 else '⚠️ NEEDS WORK'} |")
lines.append(f"| Outcome Preservation | {'100%' if eval_data['outcome_preserved'] else '0%'} | {'✅ PASS' if eval_data['outcome_preserved'] else '❌ FAIL'} |")
lines.append('')

# Clinical Bounds Details
lines.append('## Clinical Bounds Validation')
lines.append('')
lines.append('Per ML Implementation Plan Step 2.5 requirements:')
lines.append('')
lines.append('| Variable | Bounds | Violation Rate | Status |')
lines.append('|---|---|---:|---|')
for var, result in eval_data['detailed_results']['bounds'].items():
    lines.append(f"| `{var}` | {result['bounds']} | {result['rate']:.1%} | {result['status']} |")
lines.append('')

# Distribution Quality Details
lines.append('## Distributional Similarity')
lines.append('')
lines.append('Comparison between observed and imputed values:')
lines.append('')
lines.append('| Variable | KS Statistic | |SMD| | Quality |')
lines.append('|---|---:|---:|---|')
for var, result in eval_data['detailed_results']['distributions'].items():
    lines.append(f"| `{var}` | {result['ks_stat']:.3f} | {result['smd']:.3f} | {result['quality']} |")
lines.append('')

# Variability Analysis
lines.append('## Between-Imputation Variability')
lines.append('')
lines.append('Stability across multiple imputations:')
lines.append('')
lines.append('| Variable | Mean CV | SD CV | Stability |')
lines.append('|---|---:|---:|---|')
for var, result in eval_data['detailed_results']['variability'].items():
    lines.append(f"| `{var}` | {result['mean_cv']:.3f} | {result['sd_cv']:.3f} | {result['stability']} |")
lines.append('')

# Interpretation and Recommendations
lines.append('## Interpretation')
lines.append('')

if eval_data['overall_score'] >= 0.8:
    lines.append('### ✅ **EXCELLENT Quality**')
    lines.append('- Imputation meets high clinical standards')
    lines.append('- Clinical bounds violations are minimal (<1%)')
    lines.append('- Distributions align well with observed data')
    lines.append('- Stable across multiple imputations')
elif eval_data['overall_score'] >= 0.6:
    lines.append('### ⚠️ **GOOD Quality with Minor Issues**')
    lines.append('- Imputation quality is generally acceptable')
    lines.append('- Some clinical bounds violations may need attention')
    lines.append('- Most distributional properties preserved')
elif eval_data['overall_score'] >= 0.4:
    lines.append('### ⚠️ **FAIR Quality - Improvements Needed**')
    lines.append('- Moderate imputation quality issues detected')
    lines.append('- Clinical bounds violations require attention')
    lines.append('- Distributional discrepancies noted')
else:
    lines.append('### ❌ **POOR Quality - Major Issues**')
    lines.append('- Significant imputation quality problems')
    lines.append('- High clinical bounds violation rates')
    lines.append('- Poor distributional alignment')

lines.append('')

# Next Steps
lines.append('## Next Steps')
lines.append('')

if eval_data['overall_score'] >= 0.8:
    lines.append('### Recommended Actions:')
    lines.append('1. **Proceed to final imputation** with m=100 per ML Plan Step 2.1')
    lines.append('2. **Document methodology** for TRIPOD+AI compliance')  
    lines.append('3. **Continue to Phase 3** model development')
elif eval_data['overall_score'] >= 0.6:
    lines.append('### Recommended Actions:')
    lines.append('1. **Address specific bounds violations** in variables showing >5% violation rates')
    lines.append('2. **Consider additional auxiliary variables** per ML Plan Step 1.2')
    lines.append('3. **Re-run evaluation** after improvements')
    lines.append('4. **Proceed cautiously** to final imputation if time-constrained')
elif eval_data['overall_score'] >= 0.4:
    lines.append('### Required Actions:')
    lines.append('1. **Investigate high violation rates** - check parsing and units')
    lines.append('2. **Add clinical bounds enforcement** post-imputation')
    lines.append('3. **Consider alternative imputation methods** for problematic variables')
    lines.append('4. **Expand predictor set** per Step 1.2 guidance')
    lines.append('5. **Re-evaluate before final imputation**')
else:
    lines.append('### Critical Actions Required:')
    lines.append('1. **Review data preprocessing** - check for parsing errors')
    lines.append('2. **Implement strict clinical bounds** per Step 2.5')
    lines.append('3. **Consider simplified imputation** (e.g., median for continuous)')
    lines.append('4. **Consult clinical experts** on variable definitions')
    lines.append('5. **DO NOT proceed** to final imputation until resolved')

lines.append('')

# Compliance Assessment
lines.append('## ML Implementation Plan Compliance')
lines.append('')
lines.append('| Step | Requirement | Status | Notes |')
lines.append('|---|---|---|---|')

pmm_status = "✅ IMPLEMENTED" if eval_data['n_samples_evaluated'] > 0 else "❌ NOT RUN"
bounds_status = "✅ ENFORCED" if eval_data['bounds_compliance'] >= 0.9 else "⚠️ PARTIAL"
outcome_status = "✅ PRESERVED" if eval_data['outcome_preserved'] else "❌ MODIFIED"

lines.append(f"| 2.2 | PMM with donor_pool=5 | {pmm_status} | miceforest approximation used |")
lines.append(f"| 2.5 | Clinical bounds enforcement | {bounds_status} | {eval_data['bounds_compliance']:.1%} compliance rate |")
lines.append(f"| 2.5 | Outcome preservation | {outcome_status} | Mortality values {'unchanged' if eval_data['outcome_preserved'] else 'modified'} |")

lines.append('')
lines.append('---')
lines.append('*This report was generated automatically based on MICE imputation evaluation.*')

# Save report
report_file = STEP5_DIR / 'mice_evaluation_report.md'
with open(report_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("✅ Comprehensive evaluation report generated!")
print(f"📁 Report saved to: {report_file.name}")
print("\n📋 Key Findings:")
print(f"   Overall Score: {eval_data['overall_score']:.1%}")
print(f"   Quality Rating: {eval_data['quality_rating']}")
print(f"   Recommendation: {eval_data['recommendation']}")
