# A52 Dipanshu Ambilkar
import requests
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://api.open-meteo.com/v1/forecast"
p = {"latitude": 18.52, "longitude": 73.85, "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation", "forecast_days": 7}
r = requests.get(url, params=p, timeout=30).json()
h = r["hourly"]

df = pd.DataFrame({
    "time": pd.to_datetime(h["time"]),
    "temp": h["temperature_2m"],
    "humidity": h["relative_humidity_2m"],
    "wind": h["wind_speed_10m"],
    "rain": h["precipitation"],
})
print(df.shape)
print(df.isnull().sum())
df = df.dropna()
print("Avg temp:", df["temp"].mean())
print("Max temp:", df["temp"].max(), " Min temp:", df["temp"].min())

df["date"] = df["time"].dt.date
daily = df.groupby("date").agg({"temp": "mean", "humidity": "mean", "wind": "mean", "rain": "sum"})
print(daily)

plt.plot(df["time"], df["temp"])
plt.title("Temperature over 7 days - Pune")
plt.xlabel("Time")
plt.ylabel("Temp (C)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("temp_line.png")
plt.close()

daily["temp"].plot(kind="bar")
plt.title("Daily average temperature")
plt.ylabel("Temp (C)")
plt.tight_layout()
plt.savefig("temp_bar.png")
plt.close()

plt.scatter(df["temp"], df["humidity"])
plt.title("Temperature vs Humidity")
plt.xlabel("Temp (C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.savefig("temp_humidity.png")
plt.close()

sns.heatmap(df[["temp", "humidity", "wind", "rain"]].corr(), annot=True)
plt.title("Weather correlation heatmap")
plt.tight_layout()
plt.savefig("weather_corr.png")
plt.close()
print("done")
