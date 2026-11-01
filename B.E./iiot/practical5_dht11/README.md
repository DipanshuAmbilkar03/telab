# Practical 5: DHT11 Temperature and Humidity Sensor with ESP32

Aim: To interface the DHT11 sensor with the ESP32 and measure ambient temperature and humidity, displaying the readings on the Serial Monitor.

## Components
- ESP32 development board
- DHT11 sensor module
- Breadboard and jumper wires

## Wiring
- DHT11 VCC -> ESP32 3V3
- DHT11 GND -> ESP32 GND
- DHT11 DATA -> ESP32 GPIO 15

## Library needed
Install the "DHT sensor library" by Adafruit from the Arduino IDE Library Manager (Sketch > Include Library > Manage Libraries). It also installs the Adafruit Unified Sensor library it depends on.

## Board and upload
- Board: ESP32 Dev Module
- Serial Monitor: 115200

## Expected output
Temperature and humidity readings print on the Serial Monitor every 2 seconds.
