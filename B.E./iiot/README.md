# IIOT Experiments - Arduino IDE (as per IIOT manual)

These experiments follow the IIOT practicals manual. Each folder is a ready Arduino IDE sketch: the folder name and the .ino file name are the same, so open the .ino file in Arduino IDE and upload.

## One-time setup for ESP32
1. In Arduino IDE open File > Preferences.
2. In "Additional boards manager URLs" add: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
3. Open Tools > Board > Boards Manager, search esp32, install "esp32 by Espressif Systems".
4. For all practicals here select board: ESP32 Dev Module, and set the Serial Monitor to 115200.

## Practicals
- practical3_button_led: pushbutton on GPIO 4 switches an LED on GPIO 12, status on Serial Monitor.
- practical4_thingspeak_potentiometer: potentiometer on GPIO 33, readings and voltage uploaded to ThingSpeak every 15 seconds. Set your own Wi-Fi details and ThingSpeak Write API Key in the code first.
- practical5_dht11: DHT11 temperature and humidity sensor on GPIO 15. Needs the Adafruit DHT sensor library (see the practical's README).

Practical 2 is blank in the manual file (heading only, no aim or code), so it is not included here.
