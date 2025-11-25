@echo off
echo ================================================================================
echo PHASE 1, STEP 1.1: COMPREHENSIVE DATA QUALITY AUDIT
echo Focus: Mortality Prediction Model
echo ================================================================================
cd /d "C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\02_Data_Quality_Audit"
python comprehensive_data_audit.py
echo.
echo ================================================================================
echo AUDIT COMPLETE! 
echo Check output files:
echo - comprehensive_audit_report.json (detailed findings)
echo - detailed_missing_analysis.csv (all variables analysis)
echo ================================================================================
pause
