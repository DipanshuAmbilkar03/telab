# A52 Dipanshu Ambilkar
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(5)
n = 400
df = pd.DataFrame({
    "date": pd.to_datetime(np.random.choice(pd.date_range("2026-01-01", periods=180), n)),
    "region": np.random.choice(["North", "South", "East", "West"], n),
    "category": np.random.choice(["Electronics", "Clothing", "Grocery", "Furniture"], n),
    "quantity": np.random.randint(1, 10, n),
    "amount": np.round(np.random.uniform(100, 5000, n), 2),
})
print(df.head())
print(df.shape)

by_region = df.groupby("region")["amount"].sum().sort_values(ascending=False)
print(by_region)
print("Top region:", by_region.index[0])

by_region.plot(kind="bar")
plt.title("Total sales by region")
plt.ylabel("Sales (Rs)")
plt.tight_layout()
plt.savefig("sales_region_bar.png")
plt.close()

by_region.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales share by region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("sales_region_pie.png")
plt.close()

by_both = df.groupby(["region", "category"])["amount"].sum().unstack()
print(by_both)
by_both.plot(kind="bar", stacked=True)
plt.title("Sales by region and category")
plt.ylabel("Sales (Rs)")
plt.tight_layout()
plt.savefig("sales_stacked.png")
plt.close()

df["month"] = df["date"].dt.to_period("M").astype(str)
df.groupby("month")["amount"].sum().plot(kind="bar")
plt.title("Monthly sales trend")
plt.ylabel("Sales (Rs)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_monthly.png")
plt.close()
print("done")
