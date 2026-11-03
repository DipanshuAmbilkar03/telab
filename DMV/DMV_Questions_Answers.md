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

**Q7. What are the common data file formats and how are they different?**
A. CSV is plain text with values separated by commas and stores one flat table. Excel files can hold multiple sheets and cell formatting. JSON stores data as key and value pairs and can hold nested records, so it is common for web data.

**Q8. What is structured, semi-structured and unstructured data?**
A. Structured data fits a fixed table format, like CSV files and database tables. Semi-structured data has tags or keys but no strict table, like JSON and XML. Unstructured data has no fixed format, like plain text, images and audio.

**Q9. When is JSON preferred over CSV?**
A. JSON is preferred when data is nested or comes from an API, because each record can have its own keys. CSV is better for simple flat tables that are easy to open in any tool.

**Q10. What is a DataFrame?**
A. A DataFrame is the main pandas data structure. It is a two-dimensional table with labelled rows and columns, and each column can have a different data type.

**Q11. Why do we check shape, head() and dtypes after loading data?**
A. shape tells the number of rows and columns, head() shows the first few records, and dtypes shows the type of each column. Together they confirm the file loaded correctly before analysis starts.

**Q12. What does the describe() function tell about the data?**
A. describe() gives descriptive statistics for numeric columns: count, mean, standard deviation, minimum, the three quartiles and maximum. It is a quick summary of the range and spread of the data.

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

**Q7. What is the difference between data taken from files and data taken from an API?**
A. A file is static data stored locally, and it does not change until someone replaces it. An API gives live data over the internet, and parameters in the request decide which part of the data is returned.

**Q8. What does a GET request do and what are request parameters?**
A. A GET request asks the server to send data. Parameters are extra values sent with the request, like latitude, longitude and hourly variables here, which select the location and the data fields needed.

**Q9. How do we know that an API request succeeded?**
A. The response carries a status code. Code 200 means success, 404 means the address was not found, and 500 means a server side error. The JSON body can be read only after a successful response.

**Q10. Why do most APIs return data in JSON format?**
A. JSON is light in size, easy for both humans and programs to read, and it supports nested key and value pairs. Almost every language, including Python, has a built in way to parse it.

**Q11. If temperature and humidity show negative correlation, what does it mean?**
A. It means when one increases, the other tends to decrease. So on hotter hours the humidity is generally lower, and on cooler hours the humidity is generally higher.

**Q12. Why is weather data treated as time series data?**
A. The readings are recorded at regular time intervals and their order matters. The timestamp column is used to sort the data, group it by day and study how values change over time.

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

**Q7. What are the two main ways of handling missing values?**
A. The first way is deletion, where rows or columns with missing values are dropped. The second way is imputation, where missing values are filled with the mean, median or mode. Imputation is preferred when dropping would remove too much data.

**Q8. Why is the mode used to fill missing categorical values?**
A. Mean and median can only be calculated for numbers. For a category column, the mode, which is the most frequent category, is the natural value to fill.

**Q9. Why do duplicate rows harm analysis?**
A. Duplicates count the same record more than once, so totals, averages and category counts get biased. Removing them keeps every real record counted exactly once.

**Q10. What is feature engineering? Give one example from this experiment.**
A. Feature engineering means creating new useful columns from existing ones. Here avg_monthly was created by dividing total charges by tenure, and is_senior was created from the age column.

**Q11. What is the difference between standardization and normalization?**
A. Standardization converts values using mean and standard deviation, giving mean 0 and standard deviation 1. Normalization rescales values into a fixed range, usually 0 to 1. Both bring columns to a comparable scale, but the resulting ranges differ.

**Q12. Why should scaling be fitted after the train test split in a real project?**
A. If the scaler is fitted on the full data, information from the test data leaks into training. Fitting the scaler only on training data and applying it to test data keeps the evaluation honest.

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

**Q7. What is reshaping and what does pivot do?**
A. Reshaping means changing the layout of data without changing its values. A pivot rearranges a table so that values of one column become row labels and values of another become column labels, which makes summaries easier to read.

**Q8. What is the difference between merge and concat?**
A. concat simply stacks tables one below the other or side by side. merge joins two tables on a common key column, like a join in SQL, and matches rows that have the same key value.

**Q9. What is hierarchical indexing?**
A. Hierarchical indexing means using two or more levels of labels on rows or columns. For example, region as the first level and category as the second level lets one table hold grouped summaries at both levels.

**Q10. What is the difference between data cleaning and data wrangling?**
A. Data cleaning only fixes errors, like missing values, duplicates and wrong formats. Data wrangling is the wider process that also covers renaming, restructuring, merging and reshaping data into the form analysis needs.

**Q11. Why do column data types need correction during wrangling?**
A. A price stored as text cannot be averaged or summed, and a date stored as text cannot be sorted by time. Converting columns to the correct numeric or datetime type makes calculations possible.

**Q12. How can pivot_table summarize this real estate data?**
A. pivot_table with neighborhood as rows, property type as columns and sale price as values with mean aggregation gives one table. Each cell then shows the average price for that combination of area and property type.

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

**Q7. What is the difference between exploratory graphics and presentation graphics?**
A. Exploratory graphics are made during analysis to understand the data, find patterns and check problems, so they are quick and rough. Presentation graphics are made for an audience at the end, so they are polished, labelled and easy to understand.

**Q8. How do you select the right chart for a given data?**
A. A line chart shows change over time, a bar chart compares categories, a scatter plot shows the relation between two numeric variables, a box plot shows distribution and spread, and a pie chart shows share of a total. The chart is chosen from what the data needs to show.

**Q9. What is a histogram and when is it used?**
A. A histogram groups the values of one numeric column into bins and shows how many values fall in each bin. It is used to see the distribution of a variable, like whether AQI values are mostly low or spread out.

**Q10. Why are title, axis labels and legend important in a plot?**
A. They make the plot self explanatory. The title says what the plot is about, axis labels say what is measured and in which unit, and the legend identifies each line or colour when more than one series is drawn.

**Q11. What is seaborn and how is it different from matplotlib?**
A. Seaborn is a visualization library built on top of matplotlib. It gives ready statistical plots, like heatmaps and box plots, with better default styles in less code, while matplotlib gives lower level control over every part of a plot.

**Q12. What is a heatmap and when is it used?**
A. A heatmap shows values in a table or matrix using colours, where darker or stronger colour means a higher value. It is commonly used for correlation matrices and for spotting patterns in two-dimensional data.

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

**Q7. Explain the split-apply-combine strategy of groupby.**
A. In the split step, rows are divided into groups by a column value. In the apply step, a function like sum or mean is applied to each group separately. In the combine step, the group results are joined into one new table.

**Q8. What is a pivot table?**
A. A pivot table is a summary table where one field gives the rows, another field gives the columns, and the cells hold aggregated values. For example, regions as rows, categories as columns and total sales in the cells.

**Q9. What is cross tabulation?**
A. Cross tabulation, done with pd.crosstab, counts how many times each combination of two categorical values occurs. For example, it can count transactions for every pair of region and category.

**Q10. What is the difference between groupby and pivot_table?**
A. groupby is a general method that groups rows and applies any aggregation in code. pivot_table is mainly for making a two-dimensional summary table with rows, columns and values, similar to a spreadsheet report.

**Q11. Which aggregation functions are commonly used with groupby?**
A. sum gives group totals, mean gives group averages, count gives the number of records, and min, max and std give the smallest, largest and spread of values in each group.

**Q12. Why group by two columns together, like region and category?**
A. Grouping by two columns gives a summary for every combination of the two. It shows not only which region sells most, but also which category drives sales inside each region.

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

**Q7. What are the main components of a time series?**
A. The four components are trend, seasonality, cyclic variation and irregular variation. Trend is the long term direction, seasonality repeats at fixed periods, cyclic changes run over longer periods, and irregular changes are random effects.

**Q8. What is resampling in time series data?**
A. Resampling changes the frequency of the series. Daily data can be converted to weekly or monthly data using resample, with mean for prices or sum for volumes, and hourly data can similarly be converted to daily data.

**Q9. What is the difference between a rolling window and an expanding window?**
A. A rolling window always uses a fixed number of recent values, like the last 20 days, and moves forward with time. An expanding window starts from the first value and keeps growing, so it uses all past data at every step.

**Q10. What is shifting in time series data?**
A. shift() moves all values forward or backward by a given number of periods. It is used to create lag values, so today's price can be compared with yesterday's price in the same row.

**Q11. What does the alpha value do in exponential smoothing?**
A. Alpha decides how much weight the latest actual value gets. Alpha close to 1 reacts fast to recent changes and stays less smooth, while alpha close to 0 gives a smoother series that reacts slowly.

**Q12. Why is time series data never shuffled before a train test split?**
A. In time series the order carries information, and future values depend on past values. Splitting is done by time, with earlier data for training and later data for testing, so the model is tested on truly future values.

## General DMV Viva Questions

**Q1. What is data modeling?**
A. Data modeling is the process of creating a representation of the data objects of a system, the associations between them and the rules on that data. It describes the data structure, meaning and consistency constraints before a database is built.

**Q2. What are supertypes, subtypes and recursive relationships in data modeling?**
A. A supertype is a general entity and subtypes are its specialized forms, like Vehicle as supertype and Car and Truck as subtypes. A recursive relationship is a relationship of an entity with itself, like an employee who manages other employees.

**Q3. What is descriptive statistics?**
A. Descriptive statistics summarizes and describes data using numbers and graphs. It includes measures like mean, median, mode and standard deviation, along with plots like histograms and box plots.

**Q4. What is the difference between covariance and correlation?**
A. Covariance shows whether two variables move in the same or opposite direction, but its value depends on the units of the data. Correlation is the standardized form of covariance, always between minus 1 and plus 1, so strengths can be compared.

**Q5. What is the Central Limit Theorem?**
A. It states that if we take many samples and calculate the mean of each sample, those means follow a normal distribution as the sample size grows. This holds even when the original data is not normally distributed, and it is the base of many statistical tests.

**Q6. What is hypothesis testing and what are Type I and Type II errors?**
A. Hypothesis testing is a method to decide whether a claim about data is true, using a null hypothesis and an alternate hypothesis. A Type I error rejects a true null hypothesis, and a Type II error accepts a false null hypothesis.

**Q7. When are the Z-test, T-test and Chi-Square test used?**
A. A Z-test is used for means when the sample is large and variance is known. A T-test is used for means with small samples. A Chi-Square test is used for categorical data, to check independence or goodness of fit.

**Q8. What is the Monte Carlo method?**
A. Monte Carlo is a simulation method that repeats random sampling many times to estimate a result that is hard to calculate directly. The average of many random runs gives an approximate answer, like estimating the chance of an event.

**Q9. What is a Markov process?**
A. A Markov process is a random process where the next state depends only on the present state and not on the past states. Because of this memoryless property, it is used to model systems that move from one state to another over time.

**Q10. What design choices make a visualization good?**
A. The chart type should match the data, axis scales should be honest and start sensibly, and title, labels and units should be clear. Unnecessary colours and decoration should be avoided so the main pattern in the data is easy to see.

**Q11. What is data quality and what are its main aspects?**
A. Data quality means how fit the data is for its purpose. Its main aspects are accuracy, completeness with no missing values, consistency across records, and validity of formats and ranges.

**Q12. Name some data modeling tools and say what they are used for.**
A. ER/Studio, Erwin Data Modeler, LucidChart and PgModeler are data modeling tools. They are used to draw entity relationship diagrams and create logical and physical data models for databases in a visual way.
