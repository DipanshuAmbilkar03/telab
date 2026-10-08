# A52 Dipanshu Ambilkar
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

np.random.seed(2)
n = 300
df = pd.DataFrame({
    "customer_id": range(1, n + 1),
    "gender": np.random.choice(["Male", "Female", "male ", "FEMALE"], n),
    "age": np.random.randint(18, 70, n),
    "tenure": np.random.randint(1, 72, n),
    "monthly_charges": np.round(np.random.uniform(20, 120, n), 2),
    "total_charges": np.round(np.random.uniform(100, 8000, n), 2),
    "contract": np.random.choice(["Month-to-month", "One year", "Two year"], n),
    "churn": np.random.choice(["Yes", "No"], n),
})
df.loc[np.random.choice(n, 15), "age"] = np.nan
df.loc[np.random.choice(n, 10), "monthly_charges"] = np.nan
df.loc[np.random.choice(n, 5), "monthly_charges"] = 9999
df = pd.concat([df, df.iloc[:8]], ignore_index=True)

print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())

df = df.drop_duplicates()
df["age"] = df["age"].fillna(df["age"].median())
df["monthly_charges"] = df["monthly_charges"].fillna(df["monthly_charges"].median())
df["gender"] = df["gender"].str.strip().str.lower()
df["age"] = df["age"].astype(int)

q1 = df["monthly_charges"].quantile(0.25)
q3 = df["monthly_charges"].quantile(0.75)
iqr = q3 - q1
df = df[(df["monthly_charges"] >= q1 - 1.5 * iqr) & (df["monthly_charges"] <= q3 + 1.5 * iqr)]

df["avg_monthly"] = df["total_charges"] / df["tenure"]
df["is_senior"] = (df["age"] >= 60).astype(int)

num = ["age", "tenure", "monthly_charges", "total_charges", "avg_monthly"]
df[num] = StandardScaler().fit_transform(df[num])
df = pd.get_dummies(df, columns=["gender", "contract"], drop_first=True)

train, test = train_test_split(df, test_size=0.2, random_state=2)
print(train.shape, test.shape)
train.to_csv("churn_cleaned.csv", index=False)
print("done")
