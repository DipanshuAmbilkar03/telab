# IIOT Experiments - Arduino IDE

Each experiment is a ready Arduino IDE sketch: the folder name and the .ino file name are the same, so just open the .ino file in Arduino IDE and upload.

## One-time setup for ESP32 (exp1, practical3, practical4, practical5)
1. In Arduino IDE open File > Preferences.
2. In "Additional boards manager URLs" add: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
3. Open Tools > Board > Boards Manager, search esp32, install "esp32 by Espressif Systems".
4. Select board: ESP32 Dev Module. Serial Monitor: 115200.

## Experiments
- exp1_potentiometer_alert: ESP32 + potentiometer on GPIO 34, prints "warning" on Serial Monitor when the value crosses 2000. (From the Wokwi project "IIOT experiment 1". Practical 1 is not given in the manual file.)
- exp2_pir_sensor_uno: Arduino Uno + PIR sensor on D2 + LED on D13, prints motion status. Board: Arduino Uno. Serial Monitor: 9600. (From the Wokwi project "IIOT experiment 2". Practical 2 is blank in the manual file.)
- practical3_button_led: as per IIOT manual, pushbutton on GPIO 4 switches an LED on GPIO 12, status on Serial Monitor.
- practical4_thingspeak_potentiometer: as per IIOT manual, potentiometer on GPIO 33, readings and voltage uploaded to ThingSpeak every 15 seconds. Set your own Wi-Fi details and ThingSpeak Write API Key in the code first.
- practical5_dht11: DHT11 temperature and humidity sensor on GPIO 15. Needs the Adafruit DHT sensor library (see the practical's README).

Every experiment folder has a README.md with the aim, components and full wiring for performing it on hardware. exp1 and exp2 folders also keep their Wokwi diagram.json.
