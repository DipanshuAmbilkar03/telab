# A52 Dipanshu Ambilkar
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(1)
n = 120
df = pd.DataFrame({
    "OrderID": range(1, n + 1),
    "Product": np.random.choice(["Laptop", "Phone", "Tablet", "Headphones"], n),
    "Category": np.random.choice(["Electronics", "Accessories"], n),
    "Quantity": np.random.randint(1, 5, n),
    "Price": np.random.choice([999, 1499, 2499, 4999, 12999], n),
    "Region": np.random.choice(["North", "South", "East", "West"], n),
})
df.loc[np.random.choice(n, 8), "Price"] = np.nan
df = pd.concat([df, df.iloc[:5]], ignore_index=True)

df.to_csv("sales.csv", index=False)
df.to_excel("sales.xlsx", index=False)
df.to_json("sales.json", orient="records")

c = pd.read_csv("sales.csv")
e = pd.read_excel("sales.xlsx")
j = pd.read_json("sales.json")
print(c.shape, e.shape, j.shape)
print(c.isnull().sum())

c = c.drop_duplicates()
c["Price"] = c["Price"].fillna(c["Price"].median())
e = e.drop_duplicates()
e["Price"] = e["Price"].fillna(e["Price"].median())

c["Total"] = c["Quantity"] * c["Price"]
print(c.describe())
print("Total sales:", c["Total"].sum())
print("Avg order value:", c["Total"].mean())
print(c.groupby("Category")["Total"].sum())

c.groupby("Product")["Total"].sum().plot(kind="bar")
plt.title("Sales by Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_bar.png")
plt.close()

c.groupby("Region")["Total"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("sales_pie.png")
plt.close()

c.boxplot(column="Total", by="Category")
plt.title("Order value by Category")
plt.suptitle("")
plt.tight_layout()
plt.savefig("sales_box.png")
plt.close()
print("done")
