@echo off
echo ================================================================================
echo CLEANUP: Remove outdated Step 3 files (old 12-variable outputs and scripts)
echo ================================================================================
cd /d "C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\03_Variable_Classification"

echo Deleting old outputs...
if exist "final_predictor_summary.csv" del /f /q "final_predictor_summary.csv"
if exist "variable_classification_report.json" del /f /q "variable_classification_report.json"

@rem Optional: retire old script and runner (comment out if you want to keep them)
if exist "variable_classification_analysis.py" del /f /q "variable_classification_analysis.py"
if exist "run_classification.bat" del /f /q "run_classification.bat"
if exist "DELETE_OLD_FILES.txt" del /f /q "DELETE_OLD_FILES.txt"

echo Done. Remaining files are the corrected versions:
echo - corrected_variable_classification.py

echo ================================================================================
pause
