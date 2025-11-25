@echo off
echo ================================================================================
echo CORRECTED PHASE 1, STEP 1.2: VARIABLE CLASSIFICATION AND SELECTION
echo Following ML Implementation Plan: 15-25 variables per van Buuren's criteria
echo ================================================================================
cd /d "C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\03_Variable_Classification"
python corrected_variable_classification.py
echo.
echo ================================================================================
echo CORRECTED ANALYSIS COMPLETE! 
echo Check NEW output files:
echo - corrected_variable_selection.json (comprehensive analysis)
echo - corrected_predictor_summary.csv (15-25 predictors table)
echo ================================================================================
echo Generating report.md with outcome and justifications...
python build_variable_report.py
echo.
echo ================================================================================
echo REPORT COMPLETE!
echo - report.md (includes outcome presence and variable justifications)
echo ================================================================================
echo OLD INCORRECT FILES TO DELETE:
echo - final_predictor_summary.csv (only 12 variables - DELETE)
echo - variable_classification_report.json (wrong methodology - DELETE)
echo - DELETE_OLD_FILES.txt (note file)
echo If you want to remove them now, run: cleanup_step3_old_files.bat
echo ================================================================================
pause
