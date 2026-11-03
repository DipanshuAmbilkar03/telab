# Experiment 5: Industrial Data Analysis using Excel

**Aim:** Write a program for performing industrial data analysis using relevant tools and techniques.

**Software (as per manual):** Microsoft Excel. The manual downloads the IoT dataset "Farm Temperature and Humidity" from Kaggle (temperature and humidity readings taken every 1 hour for 3 months in 4 farms).

## Procedure (from the manual)
1. Select the temperature column and take 1 day of readings (24 hrs, 12 am to 12 pm next day).
2. Insert > Recommended Charts: draw the graph. Temperature peaks at 12 o'clock and falls at night.
3. Repeat with 2 days of readings (48 hrs). The peak comes again at hour 36 (24 + 12), i.e. 12 o'clock on day 2.
4. Do the same for the humidity column. Humidity rises at night and falls around 1 pm (hours 13 and 37 show the same fall).
5. Scatter plots give a clearer reading of the humidity pattern.
6. Write your observations from the graphs.

## Files here
- `farm_temperature_humidity.csv` - sample data in the same shape as the Kaggle file (timestamp, temperature, humidity; hourly readings). The original Kaggle file needs a login, so this generated sample follows the same daily pattern the manual describes.
- `exp5_data_analysis.py` - the same steps done in Python (pandas + matplotlib): 24 hrs and 48 hrs graphs for temperature and humidity.
- The 4 PNG files are the graphs the script produces.

Note: this experiment has no circuit and no Wokwi simulation; it is a data analysis practical, so the same folder is kept in both the wokwi and hardware trees only to keep the experiment list complete.
