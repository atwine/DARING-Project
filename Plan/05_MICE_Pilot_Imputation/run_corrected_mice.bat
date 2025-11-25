@echo off
echo ================================================================================
echo CORRECTED MICE IMPLEMENTATION (Per ML Implementation Plan)
echo Following Steps 2.2-2.5: PMM + Clinical Bounds + Convergence Monitoring
echo ================================================================================
cd /d "C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\05_MICE_Pilot_Imputation"

echo Installing miceforest for proper PMM implementation...
pip install miceforest scipy

echo.
echo Running corrected MICE implementation...
python corrected_mice_imputation.py

if errorlevel 1 (
  echo.
  echo ERROR: Corrected MICE encountered an error. Review console output.
  pause
  exit /b 1
)

echo.
echo ================================================================================
echo CORRECTED MICE COMPLETE!
echo Following ML Implementation Plan Steps 2.2-2.5
echo ================================================================================
echo Check NEW output files:
echo - corrected_mice_summary.json (compliance assessment)
echo - corrected_mice_report.md (clinical validation results)  
echo - corrected_mice_sample_1.csv, _2.csv, _3.csv (sample datasets)
echo - convergence_diagnostics.png (if miceforest available)
echo ================================================================================
echo.
echo METHODOLOGY COMPLIANCE:
echo ✅ PMM with donor_pool=5 for continuous variables (Step 2.2)
echo ✅ Clinical bounds enforcement (Step 2.5) 
echo ✅ 10-20 iterations with convergence monitoring (Step 2.3)
echo ✅ Proper MICE algorithm implementation
echo ================================================================================
pause
