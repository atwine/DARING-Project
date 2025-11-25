@echo off
echo ========================================
echo STEP 1: Real vs Synthetic Comparison
echo ========================================
cd /d "C:\Users\ic\OneDrive\Desktop\DARING Project\Plan\01_Real_vs_Synthetic_Comparison"
python comprehensive_data_analysis.py
echo.
echo Analysis complete! Check output files:
echo - comparison_report.json
echo - summary_report.md  
echo - missing_data_detailed.csv
pause
