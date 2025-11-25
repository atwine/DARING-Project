@echo off
echo ================================================================================
echo MICE IMPUTATION QUALITY EVALUATION
echo Comprehensive assessment of corrected MICE implementation
echo ================================================================================
cd /d "C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\05_MICE_Pilot_Imputation"

echo Running MICE evaluation...
python mice_evaluation.py

if errorlevel 1 (
  echo.
  echo ERROR: Evaluation encountered an error. Review console output.
  pause
  exit /b 1
)

echo.
echo ================================================================================
echo EVALUATION COMPLETE!
echo Check results:
echo - mice_evaluation_report.json (detailed results)
echo - Console output above shows quality assessment
echo ================================================================================
pause
