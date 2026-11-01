# IIOT Experiments - Arduino IDE

Each experiment is a ready Arduino IDE sketch: the folder name and the .ino file name are the same, so just open the .ino file in Arduino IDE and upload.

## One-time setup for ESP32 (exp1, exp3, exp4)
1. In Arduino IDE open File > Preferences.
2. In "Additional boards manager URLs" add: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
3. Open Tools > Board > Boards Manager, search esp32, install "esp32 by Espressif Systems".
4. For exp1, exp3, exp4 select board: ESP32 Dev Module.

## Experiments
- exp1_potentiometer_alert: ESP32 + potentiometer on GPIO 34, prints warning on Serial Monitor when value crosses 2000. Board: ESP32 Dev Module. Serial Monitor: 115200.
- exp2_pir_sensor_uno: Arduino Uno + PIR sensor on D2 + LED on D13. Board: Arduino Uno. Serial Monitor: 9600.
- exp3_led_webserver: ESP32 web server, control LEDs on GPIO 12 and 14 from a browser page. Board: ESP32 Dev Module. Serial Monitor: 115200. Before uploading on real hardware, change WIFI_SSID and WIFI_PASSWORD at the top of the code to your own network or hotspot. After upload, open the IP address printed on the Serial Monitor in a browser.
- exp4_potentiometer_webserver: ESP32 + potentiometer on GPIO 34, sensor value shown on a web page that refreshes every 2 seconds. Board: ESP32 Dev Module. Serial Monitor: 115200. Before uploading on real hardware, change ssid and password at the top of the code to your own network or hotspot.

Each experiment folder also has diagram.json (the Wokwi wiring file) and a README.md with the parts list and every wiring connection, for performing the same circuit on hardware.
