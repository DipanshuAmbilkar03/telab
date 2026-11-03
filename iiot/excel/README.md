# Experiment 5: Industrial Data Analysis (Excel version)

Experiment 5 of the IIOT manual is performed in Excel, not with a circuit. This folder keeps everything for it in one place:

- `exp5_excel_workbook.xlsx` - the main Excel file. Sheets: Data (full dataset as an Excel Table with color scales), Summary (live Excel formulas: AVERAGE, MAX, MIN, COUNTIF), Temp_24hrs and Temp_48hrs (line charts), Humidity_24hrs and Humidity_48hrs (line + scatter charts), Hourly_Average (column chart, line chart and data bars), Daily_Summary (daily chart and in-cell bars), Observations (manual observations and conclusion).
- `farm_temperature_humidity.csv` - the dataset used in the workbook (hourly temperature and humidity readings, sample data in the same shape as the Kaggle file from the manual; the original Kaggle file needs a login).
- `exp5_data_analysis.py` - the same steps done in Python (pandas + matplotlib), kept for reference only. The practical itself is the Excel workbook.

Main observations: temperature peaks at 12 o'clock (hour 12, and again at hour 36 in 48 hrs), humidity rises at night and falls around 1 pm (hour 13, again at hour 37).

For what to say about this Excel file in the practical/viva (aim, steps, sheet-by-sheet explanation, observations and expected questions), see `EXPLAIN_IN_PRACTICAL.md` in this folder.
