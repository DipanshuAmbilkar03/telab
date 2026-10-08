import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_squared_error

r = np.random.default_rng(42)
n = 800
a = r.uniform(1, 30, n)
b = a * r.uniform(1.5, 3.0, n)
h = r.integers(0, 24, n)
f = (30 + 12 * a + 1.5 * b) * (1 + 0.4 * ((((h >= 8) & (h <= 10)) | ((h >= 18) & (h <= 21))).astype(int))) + r.normal(0, 20, n)
d = pd.DataFrame({"distance": a, "duration": b, "hour": h, "day": r.integers(0, 7, n),
                  "passengers": r.integers(1, 5, n),
                  "peak": ((((h >= 8) & (h <= 10)) | ((h >= 18) & (h <= 21))).astype(int)), "fare": f})
i = r.choice(n, 15, replace=False)
d.loc[i[:5], "fare"] *= 10
d.loc[i[5:10], "distance"] = 200
d.loc[i[10:], "duration"] = np.nan
print("rows:", len(d))
d["duration"] = d["duration"].fillna(d["duration"].median())
d = d.dropna(subset=["fare"])
d["hour_sin"] = np.sin(2 * np.pi * d["hour"] / 24)
d["hour_cos"] = np.cos(2 * np.pi * d["hour"] / 24)
print("after cleaning:", len(d))
for c in ["fare", "distance", "duration"]:
    q1, q3, l = d[c].quantile(0.25), d[c].quantile(0.75), len(d)
    d = d[(d[c] >= q1 - 1.5 * (q3 - q1)) & (d[c] <= q3 + 1.5 * (q3 - q1))]
    print(c, "outliers removed:", l - len(d))
print(d.corr()["fare"].sort_values(ascending=False))
X, y = d.drop("fare", axis=1), d["fare"]
a, b, c, e = train_test_split(X, y, test_size=0.2, random_state=42)
s = StandardScaler()
a, b = s.fit_transform(a), s.transform(b)
nms, r2s, rms = [], [], []
for nm, md in [("Linear", LinearRegression()), ("Ridge", Ridge(alpha=1.0)), ("Lasso", Lasso(alpha=0.1))]:
    md.fit(a, c)
    p = md.predict(b)
    r2, rm = r2_score(e, p), np.sqrt(mean_squared_error(e, p))
    nms.append(nm); r2s.append(r2); rms.append(rm)
    print(nm, "R2=%.4f RMSE=%.2f" % (r2, rm))
x = np.arange(len(nms))
plt.figure()
plt.bar(x - 0.2, r2s, 0.4, label="R2")
plt.bar(x + 0.2, rms, 0.4, label="RMSE")
plt.xticks(x, nms); plt.legend(); plt.title("model comparison")
plt.savefig("model_comparison.png")
print("saved model_comparison.png")
