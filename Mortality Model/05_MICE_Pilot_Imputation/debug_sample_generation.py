"""
Debug why only 1 sample was generated instead of 30
"""
import pandas as pd
import numpy as np
from pathlib import Path

# Try to understand what happened in the MICE generation
STEP5_DIR = Path(r"C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\05_MICE_Pilot_Imputation")

# Check what samples exist
sample_files = list(STEP5_DIR.glob('corrected_mice_sample_*.csv'))
print(f"Found {len(sample_files)} sample files:")
for f in sample_files:
    df = pd.read_csv(f)
    print(f"  {f.name}: {df.shape[0]} rows, {df.shape[1]} cols")
    
    # Check age distribution in this sample
    age_vals = pd.to_numeric(df.iloc[:, df.columns.get_loc('age') if 'age' in df.columns else 1], errors='coerce')
    print(f"    Age range: {age_vals.min():.1f} - {age_vals.max():.1f}")
    print(f"    Age mean: {age_vals.mean():.1f}")

print("\n" + "="*60)
print("RECOMMENDATION:")
print("="*60)
print("1. Re-run corrected MICE with debug output")
print("2. Check miceforest kernel.num_datasets attribute")  
print("3. Verify all 30 datasets were created before extraction")
print("4. Consider simpler fallback if miceforest continues failing")
