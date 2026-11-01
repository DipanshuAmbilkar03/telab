# A52 Dipanshu Ambilkar
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(4)
dates = pd.date_range("2026-01-01", periods=90)
df = pd.DataFrame({
    "date": dates,
    "pm25": np.random.normal(80, 25, 90).clip(10, 200),
    "pm10": np.random.normal(120, 35, 90).clip(20, 300),
    "co": np.random.normal(1.2, 0.4, 90).clip(0.2, 3),
})
df["aqi"] = (df["pm25"] * 1.2 + df["pm10"] * 0.5).astype(int)
print(df.head())
print(df.describe())

plt.plot(df["date"], df["aqi"])
plt.title("AQI trend over 90 days")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("aqi_trend.png")
plt.close()

fig, ax = plt.subplots(3, 1, figsize=(8, 8), sharex=True)
ax[0].plot(df["date"], df["pm25"])
ax[0].set_title("PM2.5")
ax[1].plot(df["date"], df["pm10"])
ax[1].set_title("PM10")
ax[2].plot(df["date"], df["co"])
ax[2].set_title("CO")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("pollutants.png")
plt.close()

df.set_index("date")["aqi"].resample("W").mean().plot(kind="bar")
plt.title("Weekly average AQI")
plt.ylabel("AQI")
plt.tight_layout()
plt.savefig("aqi_weekly.png")
plt.close()

df[["pm25", "pm10", "co"]].plot(kind="box")
plt.title("Pollutant distribution")
plt.tight_layout()
plt.savefig("aqi_box.png")
plt.close()

plt.scatter(df["pm25"], df["aqi"])
plt.title("PM2.5 vs AQI")
plt.xlabel("PM2.5")
plt.ylabel("AQI")
plt.tight_layout()
plt.savefig("aqi_scatter.png")
plt.close()
print("done")
