# Practical 2: Uber Fare Prediction with Linear, Ridge and Lasso Regression (simple version)

## Aim
Predict the price of an Uber ride from trip features and compare Linear, Ridge and Lasso regression.

## Problem Statement (from the syllabus)
1. Pre-process the dataset.
2. Identify outliers.
3. Check the correlation.
4. Implement linear regression and ridge, lasso regression models.

## Steps followed
1. Build a small realistic trip dataset (seeded): distance, duration, passengers -> fare.
2. Preprocess: drop missing values.
3. Outliers: IQR rule on the fare column.
4. Correlation of each feature with fare (printed).
5. Train Linear, Ridge and Lasso on a train/test split; compare R2 and RMSE.

## Output
- Distance and duration show the strongest correlation with fare.
- All three models reach R2 close to 1.0 on this clean data; the printed table shows the small differences between them.
