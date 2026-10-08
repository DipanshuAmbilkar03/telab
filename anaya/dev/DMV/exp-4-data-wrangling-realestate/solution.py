# A52 Dipanshu Ambilkar
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(3)
n = 250
df = pd.DataFrame({
    "Property ID": range(1, n + 1),
    "Neighborhood ": np.random.choice(["Aundh", "Kothrud", "Wakad", "Hinjewadi"], n),
    "Property-Type": np.random.choice(["Flat", "Villa", "Plot"], n),
    "Area (sqft)": np.random.randint(500, 3000, n),
    " Bedrooms": np.random.randint(1, 5, n),
    "Sale Price (Rs)": np.random.randint(3000000, 20000000, n),
    "Year Built": np.random.randint(1990, 2024, n),
})
df.loc[np.random.choice(n, 12), "Area (sqft)"] = np.nan
df.loc[np.random.choice(n, 4), "Sale Price (Rs)"] = 90000000

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "").str.replace("-", "_")
print(list(df.columns))
print(df.isnull().sum())

df["area_sqft"] = df["area_sqft"].fillna(df["area_sqft"].median())

q1 = df["sale_price_rs"].quantile(0.25)
q3 = df["sale_price_rs"].quantile(0.75)
iqr = q3 - q1
df = df[df["sale_price_rs"] <= q3 + 1.5 * iqr]
print("after outlier removal:", df.shape)

flats = df[df["property_type"] == "Flat"]
print("flats only:", flats.shape)

avg_nb = df.groupby("neighborhood")["sale_price_rs"].mean().sort_values()
avg_type = df.groupby("property_type")["sale_price_rs"].mean()
print(avg_nb)
print(avg_type)

avg_nb.plot(kind="bar")
plt.title("Average sale price by neighborhood")
plt.ylabel("Price (Rs)")
plt.tight_layout()
plt.savefig("price_neighborhood.png")
plt.close()

df = pd.get_dummies(df, columns=["neighborhood", "property_type"], drop_first=True)
print("encoded shape:", df.shape)
print("done")
