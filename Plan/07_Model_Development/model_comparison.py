"""
Step 7: Model Development - Multi-Model Comparison
==================================================
Pre-specified: Logistic Regression vs Elastic Net vs Random Forest

MODEL SELECTION CRITERIA (pre-specified):
1. Calibration slope closest to 1.0
2. C-statistic (if calibration similar)
3. Simplicity/interpretability (if performance similar)

References: Rubin (1987), Steyerberg (2019), Collins et al. BMJ 2024, TRIPOD+AI
"""
import json
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import roc_auc_score, brier_score_loss, roc_curve
from sklearn.calibration import calibration_curve
from scipy import stats
import matplotlib.pyplot as plt

# Paths
PLAN_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan")
STEP6_DIR = PLAN_DIR / "06_Final_Imputation"
STEP7_DIR = PLAN_DIR / "07_Model_Development"
IMPUTED_DIR = STEP6_DIR / "imputed_data"

def rubins_rules(estimates, variances):
    m = len(estimates)
    Q_bar = np.mean(estimates)
    U_bar = np.mean(variances)
    B = np.var(estimates, ddof=1)
    T = U_bar + (1 + 1/m) * B
    SE = np.sqrt(T)
    nu = max((m - 1) * (1 + U_bar/((1+1/m)*B))**2 if B > 0 else 1000, 1)
    t_crit = stats.t.ppf(0.975, df=nu)
    return Q_bar, SE, Q_bar - t_crit * SE, Q_bar + t_crit * SE

def pool_cstatistic(c_values, se_values=None):
    c_values = np.clip(np.array(c_values), 0.501, 0.999)
    logit_c = np.log(c_values / (1 - c_values))
    se_values = np.array(se_values) if se_values else np.full(len(c_values), 0.03)
    logit_var = (se_values ** 2) / (c_values * (1 - c_values)) ** 2
    q, _, ci_lo, ci_hi = rubins_rules(logit_c, logit_var)
    return 1/(1+np.exp(-q)), 1/(1+np.exp(-ci_lo)), 1/(1+np.exp(-ci_hi))

def calc_auc_se(y, pred):
    auc = roc_auc_score(y, pred)
    n1, n0 = y.sum(), len(y) - y.sum()
    q1, q2 = auc/(2-auc), 2*auc**2/(1+auc)
    se = np.sqrt((auc*(1-auc) + (n1-1)*(q1-auc**2) + (n0-1)*(q2-auc**2))/(n1*n0))
    return auc, se

def calc_calibration(y, pred):
    log_odds = np.clip(np.log(np.clip(pred,1e-10,1-1e-10)/(1-np.clip(pred,1e-10,1-1e-10))), -10, 10)
    m = LogisticRegression(penalty=None, solver='lbfgs', max_iter=1000)
    m.fit(log_odds.reshape(-1,1), y)
    return m.coef_[0][0], m.intercept_[0]

def preprocess(df, feature_cols, outcome):
    X = df[feature_cols].copy()
    for col in X.select_dtypes(include=['object','category']).columns:
        X[col] = LabelEncoder().fit_transform(X[col].fillna('Unknown').astype(str))
    X = X.fillna(X.median()).replace([np.inf,-np.inf], np.nan).fillna(X.median())
    return X.values, df[outcome].values

# Load datasets
print("="*70)
print("STEP 7: MODEL COMPARISON")
print("="*70)

datasets = [pd.read_csv(p) for p in sorted(IMPUTED_DIR.glob("imputed_dataset_*.csv"))]
M = len(datasets)
print(f"\nLoaded {M} imputed datasets")

if M == 0:
    raise RuntimeError("No datasets found. Run Step 6 first.")

OUTCOME = 'mortality'
feature_cols = [c for c in datasets[0].columns if c != OUTCOME]
print(f"Features: {len(feature_cols)}, Samples: {len(datasets[0])}")

# Fit models
results = {'lr': {'aucs':[],'ses':[],'preds':[],'coefs':[]},
           'en': {'aucs':[],'ses':[],'preds':[],'coefs':[]},
           'rf': {'aucs':[],'ses':[],'preds':[]}}

scaler = StandardScaler()
X0, _ = preprocess(datasets[0], feature_cols, OUTCOME)
scaler.fit(X0)

print("\nFitting models...")
for i, df in enumerate(datasets):
    X, y = preprocess(df, feature_cols, OUTCOME)
    Xs = scaler.transform(X)
    
    # Logistic
    lr = LogisticRegression(penalty='l2', C=1.0, max_iter=1000, random_state=42)
    lr.fit(Xs, y)
    pred_lr = lr.predict_proba(Xs)[:,1]
    auc_lr, se_lr = calc_auc_se(y, pred_lr)
    results['lr']['aucs'].append(auc_lr)
    results['lr']['ses'].append(se_lr)
    results['lr']['preds'].append(pred_lr)
    results['lr']['coefs'].append(lr.coef_[0])
    
    # Elastic Net
    en = LogisticRegression(penalty='elasticnet', solver='saga', l1_ratio=0.5, C=1.0, max_iter=2000, random_state=42)
    en.fit(Xs, y)
    pred_en = en.predict_proba(Xs)[:,1]
    auc_en, se_en = calc_auc_se(y, pred_en)
    results['en']['aucs'].append(auc_en)
    results['en']['ses'].append(se_en)
    results['en']['preds'].append(pred_en)
    results['en']['coefs'].append(en.coef_[0])
    
    # Random Forest
    rf = RandomForestClassifier(n_estimators=200, max_depth=8, min_samples_leaf=10, random_state=42, n_jobs=-1)
    rf.fit(Xs, y)
    pred_rf = rf.predict_proba(Xs)[:,1]
    auc_rf, se_rf = calc_auc_se(y, pred_rf)
    results['rf']['aucs'].append(auc_rf)
    results['rf']['ses'].append(se_rf)
    results['rf']['preds'].append(pred_rf)
    
    if (i+1) % 20 == 0:
        print(f"  {i+1}/{M} | LR:{auc_lr:.3f} EN:{auc_en:.3f} RF:{auc_rf:.3f}")

# Pool results
y_true = datasets[0][OUTCOME].values
print("\n" + "="*70)
print("POOLED RESULTS")
print("="*70)

models = {}
for name, key in [('Logistic Regression','lr'), ('Elastic Net','en'), ('Random Forest','rf')]:
    pred = np.mean(results[key]['preds'], axis=0)
    c, c_lo, c_hi = pool_cstatistic(results[key]['aucs'], results[key]['ses'])
    brier = brier_score_loss(y_true, pred)
    cal_slope, _ = calc_calibration(y_true, pred)
    models[name] = {'c':c, 'c_lo':c_lo, 'c_hi':c_hi, 'brier':brier, 'cal':cal_slope, 'pred':pred}
    print(f"\n{name}:")
    print(f"  C-statistic: {c:.4f} ({c_lo:.4f}-{c_hi:.4f})")
    print(f"  Calibration: {cal_slope:.4f}")
    print(f"  Brier: {brier:.4f}")

# Model selection
print("\n" + "="*70)
print("MODEL SELECTION")
print("="*70)
cal_diff = {n: abs(m['cal']-1) for n,m in models.items()}
c_range = max(m['c'] for m in models.values()) - min(m['c'] for m in models.values())

if c_range < 0.02:
    selected = 'Logistic Regression'
    reason = "Similar performance (ΔC<0.02); prefer simpler model"
else:
    selected = min(cal_diff, key=cal_diff.get)
    reason = f"Best calibration (|slope-1|={cal_diff[selected]:.3f})"

print(f"\n✅ Selected: {selected}")
print(f"   Reason: {reason}")

# Comparison table
comp = pd.DataFrame([
    {'Model':n, 'C-statistic':f"{m['c']:.3f} ({m['c_lo']:.3f}-{m['c_hi']:.3f})",
     'Cal.Slope':f"{m['cal']:.3f}", 'Brier':f"{m['brier']:.4f}"}
    for n,m in models.items()
])
print("\n" + comp.to_string(index=False))
comp.to_csv(STEP7_DIR / 'model_comparison.csv', index=False)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for n,m in models.items():
    fpr,tpr,_ = roc_curve(y_true, m['pred'])
    axes[0].plot(fpr, tpr, label=f"{n} ({m['c']:.3f})")
axes[0].plot([0,1],[0,1],'k--')
axes[0].set_xlabel('FPR'); axes[0].set_ylabel('TPR')
axes[0].set_title('ROC Curves'); axes[0].legend(); axes[0].grid(alpha=0.3)

for n,m in models.items():
    prob_true, prob_pred = calibration_curve(y_true, m['pred'], n_bins=10)
    axes[1].plot(prob_pred, prob_true, 'o-', label=n)
axes[1].plot([0,1],[0,1],'k--')
axes[1].set_xlabel('Predicted'); axes[1].set_ylabel('Observed')
axes[1].set_title('Calibration'); axes[1].legend(); axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig(STEP7_DIR / 'model_comparison.png', dpi=150)
print(f"\n✅ Saved: model_comparison.png")

# Save results
json.dump({
    'date': datetime.now().isoformat(), 'n_imputations': M,
    'selected_model': selected, 'reason': reason,
    'results': {n: {'c':m['c'],'c_ci':[m['c_lo'],m['c_hi']],'cal':m['cal'],'brier':m['brier']} 
                for n,m in models.items()}
}, open(STEP7_DIR / 'model_results.json', 'w'), indent=2)

# Save LR coefficients
coefs = np.mean(results['lr']['coefs'], axis=0)
pd.DataFrame({'Variable':feature_cols[:len(coefs)], 'Coefficient':coefs}).to_csv(
    STEP7_DIR / 'logistic_coefficients.csv', index=False)

print(f"\n{'='*70}")
print("COMPLETE")
print(f"{'='*70}")
