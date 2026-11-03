# Experiment 5 (Excel): What to Explain in the Practical

Use this as your speaking guide when the examiner opens the Excel file or asks you to explain Experiment 5.

## Start with this (the aim, say it first)

"Sir, Experiment 5 is industrial data analysis using Excel. I have taken the Farm Temperature and Humidity dataset, which contains hourly temperature and humidity readings recorded by sensors on farms. I analyzed the data in Excel using charts, and from the charts I have written observations about the daily pattern of temperature and humidity."

This one answer covers: what the experiment is, what data you used, what tool you used, and what you produced.

## Steps to explain (what you did, in order)

1. Downloaded the IoT dataset "Farm Temperature and Humidity" (as given in the manual). It has three columns: Timestamp, Temperature and Humidity, with readings taken every 1 hour.
2. Selected the temperature readings of 1 day (24 hours) and drew the graph using Insert > Recommended Charts.
3. Repeated the same for 2 days of readings (48 hours) to check whether the pattern repeats.
4. Did the same steps for the humidity column (24 hours and 48 hours), and also made scatter plots for humidity because the pattern is clearer in a scatter plot.
5. Wrote the observations from the graphs, and added some extra analysis sheets (hourly average, daily summary, formula summary) to confirm the same pattern on the full data.

## Sheet by sheet: what to say

**Data**
"This is the complete dataset, 720 hourly readings. I have formatted it as an Excel Table so filters can be applied. The color scales are conditional formatting: in Temperature, green is low and red is high, so hot hours stand out directly in the data itself, without opening any chart."

**Temp_24hrs**
"This is the temperature graph of 1 day. Temperature rises in the day and peaks at 12 o'clock with 32.5, then falls and is lowest at night."

**Temp_48hrs**
"This is 2 days of temperature. The peak comes again at hour 36, which is 24 + 12, that is again 12 o'clock on the second day, and there is a minimum at hour 24, midnight. So the pattern repeats every 24 hours."

**Humidity_24hrs and Humidity_48hrs**
"Humidity behaves opposite to temperature: it rises at night and falls around 1 pm. In the 48 hours data, the fall appears at hour 13 and again at hour 37, that is 1 pm on the next day. The scatter plots on these sheets show the same pattern more clearly."

**Hourly_Average**
"Here I averaged the readings of every hour of the day across all days using Excel. The column chart of average temperature and the line chart of average humidity confirm the same thing on the full data: average temperature is highest near noon and average humidity is highest at night. Data bars are also applied on the average temperature column."

**Daily_Summary**
"For every day I have calculated average, maximum and minimum temperature and average humidity. The chart shows the daily average temperature of all 30 days, and the in-cell bars give a quick visual of each day's average."

**Summary**
"This sheet uses Excel formulas directly on the Data sheet: AVERAGE, MAX, MIN and COUNTIF. For example, overall average temperature and humidity, and counts like how many readings had temperature above 30 or humidity above 80. If the data changes, this sheet updates automatically because it is formula based."

**Observations**
"All observations and the conclusion are written here, based on the graphs."

## Observations to speak (memorize these numbers)

- Temperature peak: hour 12 (value 32.5), i.e. 12 o'clock noon.
- Second peak in 48 hours: hour 36 (24 + 12).
- Temperature minimum: at night, hour 24 in the 48 hours graph is midnight.
- Humidity: rises at night, falls around 1 pm; fall repeats at hour 13 and hour 37 (24 + 13).
- Both temperature and humidity follow a daily (24 hour) cycle.

## If the examiner asks these, answer like this

**Why Excel for this experiment?**
"The aim says analysis using relevant tools, and the manual uses Excel. Excel is enough for this size of data: charts, formulas and formatting give the patterns and summary without any programming."

**Why draw graphs instead of reading values?**
"There are hundreds of readings, no pattern is visible in raw numbers. In a graph, peaks, falls and the repeating cycle are visible at a glance. That is data visualization."

**Why a scatter plot for humidity?**
"The manual itself suggests scatter plots for humidity. The scatter plot spreads the points clearly, so the rise at night and fall at noon is easier to see than in the table."

**What is IoT data analytics (in this experiment's context)?**
"Collecting sensor data, storing it, processing it, analyzing it for patterns, and visualizing it. This experiment does exactly that: farm sensor data is collected in the dataset, analyzed in Excel, and shown as charts for decisions, for example when to irrigate."

**What is the conclusion?**
"Temperature peaks at 12 o'clock and falls at night, humidity rises at night and falls around 1 pm, and both patterns repeat daily. So industrial/farm IoT data can be analyzed in Excel to get useful observations for decision making."

## Closing line (finish with this)

"So, Sir, in this experiment I performed IoT data analysis of farm temperature and humidity using Excel tools and techniques, and the daily pattern of both temperature and humidity is clearly visible from the charts."
