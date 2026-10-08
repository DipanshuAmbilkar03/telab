# A52 Dipanshu Ambilkar
"""
Practical 2 - Uber fare prediction (simple version)
Requirements: preprocess the data, find outliers, check correlation,
then train Linear, Ridge and Lasso regression models and compare them.
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_squared_error

# 1. Make a small realistic dataset (seeded so it is the same every run)
rng = np.random.default_rng(7)
n = 500
distance = rng.uniform(1, 30, n)             # km
duration = distance * rng.uniform(1.5, 3, n)  # minutes
passengers = rng.integers(1, 5, n)
fare = 30 + 12 * distance + 1.5 * duration + rng.normal(0, 15, n)

df = pd.DataFrame({"distance": distance, "duration": duration,
                   "passengers": passengers, "fare": fare})

# 2. Preprocess: drop missing values
df = df.dropna()
print("Rows after cleaning:", len(df))

# 3. Outliers: IQR rule on the fare column
q1, q3 = df["fare"].quantile([0.25, 0.75])
iqr = q3 - q1
outliers = df[(df["fare"] < q1 - 1.5 * iqr) | (df["fare"] > q3 + 1.5 * iqr)]
print("Outliers found:", len(outliers))
df = df.drop(outliers.index)

# 4. Correlation of every feature with fare
print("\nCorrelation with fare:")
print(df.corr()["fare"].round(3))

# 5. Train the three models and compare
X = df[["distance", "duration", "passengers"]]
y = df["fare"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7)

for name, model in [("Linear", LinearRegression()),
                    ("Ridge", Ridge()),
                    ("Lasso", Lasso())]:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    r2 = r2_score(y_test, pred)
    rmse = mean_squared_error(y_test, pred) ** 0.5
    print(f"{name:7s}  R2 = {r2:.4f}   RMSE = {rmse:.2f}")
