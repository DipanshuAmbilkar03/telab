# Practical 4: Potentiometer Data to ThingSpeak with ESP32 (as per IIOT manual)

Aim: To read a potentiometer using ESP32, convert the reading to voltage, and upload both values to a ThingSpeak channel every 15 seconds.

## Components
- ESP32 development board
- Potentiometer (10k)
- Breadboard and jumper wires

## Wiring
- Potentiometer one outer pin -> ESP32 3V3
- Potentiometer other outer pin -> ESP32 GND
- Potentiometer middle pin (wiper) -> ESP32 GPIO 33

## Before uploading
- Create a free channel on thingspeak.com with two fields enabled.
- In the code, replace ssid and password with your Wi-Fi or hotspot details.
- Replace apiKey with the Write API Key of your own channel. The key in the code is the demo key printed in the manual.

## Board and upload
- Board: ESP32 Dev Module
- Serial Monitor: 115200

## Expected output
The Serial Monitor shows the potentiometer value (0 to 4095), the voltage (0 to 3.3), and an HTTP response code of 200. The ThingSpeak channel graphs update every 15 seconds when the potentiometer is turned.
