# DMV Practicals: Viva Questions and Answers

## Experiment 1: Data Loading, Storage and File Formats

**Q1. Which pandas functions are used to read CSV, Excel and JSON files?**
A. read_csv() reads CSV files, read_excel() reads Excel files and read_json() reads JSON files. All three return a DataFrame, so the same analysis code works on every format.

**Q2. How did you create the three sales files from one dataset?**
A. One DataFrame was built in Python and saved with to_csv(), to_excel() and to_json(). The JSON file used orient="records", so each row became one JSON object.

**Q3. What data quality issues were present in the sales data and how were they fixed?**
A. The data had 5 duplicate rows and 8 missing Price values. Duplicates were removed with drop_duplicates() and missing prices were filled with the median price using fillna().

**Q4. Why is the median used to fill missing values instead of the mean?**
A. The median is not affected much by very large or very small values. Prices can have outliers, so the median gives a safer central value for filling.

**Q5. How were total sales and average order value calculated?**
A. A new column Total was derived as Quantity multiplied by Price. Total sales is the sum of the Total column and average order value is its mean.

**Q6. Which plots were used in this experiment and what does each show?**
A. A bar plot showed total sales by product, a pie chart showed the share of sales by region, and a box plot showed how order value is distributed for each category.

## Experiment 2: Interacting with Web APIs

**Q1. What is an API and how did this experiment get weather data?**
A. An API is a service that returns data over the internet when a request is sent. The requests library sent a GET request to the Open-Meteo API with latitude, longitude and the required hourly variables as parameters.

**Q2. What format does the API return and how was it converted for analysis?**
A. The API returns data in JSON format. The hourly section of the JSON was picked out and converted into a pandas DataFrame with time, temperature, humidity, wind speed and precipitation columns.

**Q3. Which weather parameters were analyzed?**
A. Temperature, relative humidity, wind speed and precipitation were analyzed for Pune over 7 days, at hourly level.

**Q4. How were daily weather statistics calculated?**
A. A date column was derived from the timestamp and groupby was applied on it. Mean temperature, humidity and wind were calculated per day, and rainfall was summed per day.

**Q5. What does the correlation heatmap show in this experiment?**
A. The heatmap shows correlation values between temperature, humidity, wind and rain. It helps to see, for example, whether humidity rises when temperature falls.

**Q6. Why is dropna() applied after loading API data?**
A. API data can contain missing readings for some hours. dropna() removes those rows so that averages and plots are not affected by empty values.

## Experiment 3: Data Cleaning and Preparation

**Q1. What is data cleaning and why is it needed before analysis?**
A. Data cleaning means fixing problems like missing values, duplicates, wrong formats and outliers. Models and analysis give wrong results if the data is dirty, so cleaning is done first.

**Q2. What problems were present in the churn dataset?**
A. The dataset had duplicate rows, missing age and monthly charges values, inconsistent gender values like "male " and "FEMALE", and outlier charges such as 9999.

**Q3. How were the inconsistent gender values corrected?**
A. The str.strip() method removed extra spaces and str.lower() converted all values to lowercase. After this, "male ", "Male" and "MALE" all became one single category.

**Q4. How were outliers detected and removed in this experiment?**
A. The IQR method was used on monthly charges. Values below Q1 minus 1.5 times IQR or above Q3 plus 1.5 times IQR were treated as outliers and removed.

**Q5. What is the difference between label encoding and one-hot encoding?**
A. Label encoding gives each category a number, which can wrongly suggest an order. One-hot encoding creates a separate 0 or 1 column per category, and here get_dummies() was used for gender and contract.

**Q6. Why is StandardScaler applied and what is train test split?**
A. StandardScaler brings all numeric columns to a similar scale, with mean 0 and standard deviation 1, so large columns do not dominate. Train test split divides the cleaned data into 80 percent training data and 20 percent test data.

## Experiment 4: Data Wrangling on Real Estate Market

**Q1. What is data wrangling?**
A. Data wrangling is the process of converting raw, messy data into a clean and usable form. It includes renaming columns, fixing data types, handling missing values and removing outliers.

**Q2. How were the messy column names cleaned in this experiment?**
A. Spaces were stripped, names were converted to lowercase, and spaces, brackets and hyphens were replaced with underscores. For example, "Sale Price (Rs)" became "sale_price_rs".

**Q3. Why is a uniform column naming style important?**
A. Clean names are easy to type and use in code without errors. Messy names with spaces or brackets need special syntax every time the column is used.

**Q4. How were missing area values and price outliers handled?**
A. Missing area values were filled with the median area. Sale prices above the upper IQR limit were removed as outliers, because a few extreme prices can distort the average price.

**Q5. What did the groupby analysis show in this experiment?**
A. Average sale price was calculated for each neighborhood and each property type. This shows which areas are costly and which property type sells at a higher average price.

**Q6. Why was one-hot encoding applied at the end?**
A. Machine learning models cannot use text columns directly. get_dummies() converted neighborhood and property type into numeric 0 or 1 columns so the data is ready for modeling.

## Experiment 5: Data Visualization using Matplotlib

**Q1. What is AQI and which pollutants were used in this experiment?**
A. AQI is the Air Quality Index, a single number that shows how polluted the air is. PM2.5, PM10 and carbon monoxide (CO) values over 90 days were used to compute AQI.

**Q2. What is matplotlib and what is a figure in it?**
A. Matplotlib is the main Python library for static plots. A figure is the full plotting area or window, and axes are the individual plots drawn inside the figure.

**Q3. Why were subplots used for the pollutants?**
A. Three subplots in one figure plotted PM2.5, PM10 and CO one below the other with a shared x-axis. This makes it easy to compare how all three pollutants changed on the same dates.

**Q4. How was weekly average AQI calculated and plotted?**
A. The date column was set as index and resample("W") grouped the data by week. The mean AQI of each week was then plotted as a bar chart.

**Q5. What does a box plot show and why was it used for pollutants?**
A. A box plot shows the median, quartiles and spread of data, along with outlier points. It was used to compare the distribution and variability of PM2.5, PM10 and CO.

**Q6. What does the PM2.5 versus AQI scatter plot tell us?**
A. Each point is one day, with PM2.5 on the x-axis and AQI on the y-axis. The upward pattern shows that as PM2.5 increases, AQI also increases.

## Experiment 6: Data Aggregation

**Q1. What is data aggregation?**
A. Aggregation means summarizing detailed data into totals or averages for groups. Here 400 retail transactions were summarized by region, category and month.

**Q2. Which pandas method is mainly used for aggregation?**
A. The groupby() method groups rows by one or more columns, and then sum(), mean() or count() is applied on the groups. In this experiment amounts were summed per group.

**Q3. How was the top performing region found?**
A. Sales amount was summed for each region and sorted in descending order. The first region in the sorted result, shown by by_region.index[0], is the top performer.

**Q4. What is the difference between the bar chart and pie chart used here?**
A. The bar chart compares the actual total sales of the four regions. The pie chart shows each region's percentage share of the total sales.

**Q5. What is a stacked bar chart and what did it show?**
A. A stacked bar chart places category sales one above the other inside each region's bar. It showed both the total sales of a region and how each category contributed to it.

**Q6. How was the monthly sales trend obtained?**
A. A month column was extracted from the transaction date using dt.to_period("M"). Sales were then grouped and summed by month and plotted as a bar chart.

## Experiment 7: Time Series Analysis of Stock Market Data

**Q1. What is time series data?**
A. Time series data is a sequence of values recorded in time order, like daily stock prices. The order matters, because each value depends on the time at which it was recorded.

**Q2. What is a moving average and why are 20-day and 50-day averages used?**
A. A moving average is the average of the last few values, which smooths daily ups and downs. The 20-day average shows the short term trend and the 50-day average shows the longer term trend.

**Q3. How were moving averages calculated in pandas?**
A. The rolling() method created a moving window on the closing price column. rolling(20).mean() gave the 20-day moving average and rolling(50).mean() gave the 50-day one.

**Q4. What is seasonality and how was it checked here?**
A. Seasonality is a pattern that repeats at fixed periods, such as months. Average closing price was calculated for each month and plotted, to see if some months regularly show higher prices.

**Q5. What does the price and volume correlation value indicate?**
A. Correlation tells whether price and volume move together. A positive value means price tends to rise when volume is high, and a value near zero means there is no strong relation.

**Q6. How was the 30-day forecast made in this experiment?**
A. Exponential smoothing was applied on the closing price with alpha 0.3, giving more weight to recent values. The last smoothed value and the recent trend were extended for 30 future days to draw the forecast.
