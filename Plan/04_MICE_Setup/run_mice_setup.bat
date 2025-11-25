@echo off
echo ================================================================================
echo PHASE 2: MICE SETUP (Step 2.1 - 2.3)
echo Compute number of imputations and build predictor matrix including OUTCOME
echo ================================================================================
cd /d "C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\04_MICE_Setup"
python mice_setup.py
if errorlevel 1 (
  echo.
  echo ERROR: MICE setup encountered an error. Review console output.
  pause
  exit /b 1
)

echo.
echo ================================================================================
echo MICE SETUP COMPLETE!
echo Check output files:
echo - mice_config.json (imputation counts and methods)
echo - imputation_matrix.csv (predictor inclusion; includes OUTCOME for all)
echo - setup_report.md / report.md (documentation)
echo ================================================================================
pause
