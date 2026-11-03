# Connections: All Experiments (Actual Hardware)

## Experiment 1: Alert Message using Potentiometer (ESP32)
- ESP32 -> Laptop via USB cable (power, upload, Serial Monitor)
- Potentiometer middle pin (signal) -> GPIO 34
- Potentiometer one side pin (red) -> 3.3V
- Potentiometer other side pin (orange) -> GND

## Experiment 2: PIR Sensor with Arduino Uno
- Arduino Uno -> Laptop via USB cable (power, upload, Serial Monitor)
- PIR GND -> Arduino GND
- PIR VCC -> Arduino 5V
- PIR OUT (signal) -> Arduino pin 2
- LED anode (long leg) -> Arduino pin 13, through a 220 ohm resistor
- LED cathode (short leg) -> Arduino GND

## Experiment 3: LED Web Server (ESP32)
- ESP32 -> Laptop via USB cable; phone/laptop on the same Wi-Fi hotspot opens the web page
- GPIO 12 -> 220 ohm resistor -> LED 1 anode (long leg); LED 1 cathode -> GND
- GPIO 14 -> 220 ohm resistor -> LED 2 anode (long leg); LED 2 cathode -> GND

## Experiment 4: Potentiometer Web Server (ESP32)
- ESP32 -> Laptop via USB cable; phone/laptop on the same Wi-Fi hotspot opens the web page
- Potentiometer middle pin (signal) -> GPIO 34
- Potentiometer one side pin (red) -> 3.3V
- Potentiometer other side pin (orange) -> GND

## Experiment 5: Industrial Data Analysis using Excel
- No circuit and no connections. It is a data analysis practical on the Farm Temperature and Humidity dataset in Excel.

Each experiment folder (Exp 1 to 4) also has its own `connections.txt` and `diagram.json` with the same wiring.
