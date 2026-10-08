import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_squared_error

rng = np.random.default_rng(42)
n = 800
distance = rng.uniform(1, 30, n)
duration = distance * rng.uniform(1.5, 3.0, n)
hour = rng.integers(0, 24, n)
day = rng.integers(0, 7, n)
passengers = rng.integers(1, 5, n)
peak = (((hour >= 8) & (hour <= 10)) | ((hour >= 18) & (hour <= 21))).astype(int)
surge = 1 + 0.4 * peak
fare = (30 + 12 * distance + 1.5 * duration) * surge + rng.normal(0, 20, n)

df = pd.DataFrame({
    "distance": distance, "duration": duration, "hour": hour,
    "day": day, "passengers": passengers, "peak": peak, "fare": fare
})

idx = rng.choice(n, 15, replace=False)
df.loc[idx[:5], "fare"] = df.loc[idx[:5], "fare"] * 10
df.loc[idx[5:10], "distance"] = 200
df.loc[idx[10:], "duration"] = np.nan
print("rows:", len(df))

df["duration"] = df["duration"].fillna(df["duration"].median())
df = df.dropna(subset=["fare"])
df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
print("after cleaning:", len(df))

for col in ["fare", "distance", "duration"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    before = len(df)
    df = df[(df[col] >= q1 - 1.5 * iqr) & (df[col] <= q3 + 1.5 * iqr)]
    print(col, "outliers removed:", before - len(df))

print(df.corr()["fare"].sort_values(ascending=False))

X = df.drop("fare", axis=1)
y = df["fare"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

names = []
r2s = []
rmses = []
for name, model in [("Linear", LinearRegression()), ("Ridge", Ridge(alpha=1.0)), ("Lasso", Lasso(alpha=0.1))]:
    model.fit(X_train_s, y_train)
    pred = model.predict(X_test_s)
    r2 = r2_score(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    names.append(name)
    r2s.append(r2)
    rmses.append(rmse)
    print(name, "R2=%.4f RMSE=%.2f" % (r2, rmse))

x = np.arange(len(names))
plt.figure()
plt.bar(x - 0.2, r2s, 0.4, label="R2")
plt.bar(x + 0.2, rmses, 0.4, label="RMSE")
plt.xticks(x, names)
plt.legend()
plt.title("model comparison")
plt.savefig("model_comparison.png")
print("saved model_comparison.png")
