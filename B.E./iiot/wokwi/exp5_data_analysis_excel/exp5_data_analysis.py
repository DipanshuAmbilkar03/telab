# Experiment 5: Industrial Data Analysis (manual does this in Excel)
# Same steps in Python: 24 hrs and 48 hrs graphs for Temperature and Humidity
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("farm_temperature_humidity.csv", parse_dates=["timestamp"])
print("Total rows:", len(df))
print(df.head())

day1 = df.head(24)
day2 = df.head(48)

plt.figure(figsize=(10, 4))
plt.plot(day1["timestamp"], day1["temperature"], marker="o")
plt.title("Temperature - 24 hrs (1 day)")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temp_24hrs.png")
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(day2["timestamp"], day2["temperature"], marker="o")
plt.title("Temperature - 48 hrs (2 days)")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temp_48hrs.png")
plt.show()

plt.figure(figsize=(10, 4))
plt.scatter(day1["timestamp"], day1["humidity"], color="green")
plt.title("Humidity - 24 hrs (1 day)")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("humidity_24hrs.png")
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(day2["timestamp"], day2["humidity"], marker="x", color="green")
plt.title("Humidity - 48 hrs (2 days)")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("humidity_48hrs.png")
plt.show()

peak_hour = day1.loc[day1["temperature"].idxmax(), "timestamp"].hour
print("Day 1 temperature peak at hour:", peak_hour)
print("Day 1 max temperature:", day1["temperature"].max())
print("Day 1 min temperature:", day1["temperature"].min())
