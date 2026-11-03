# Experiment 3: User Interface for Monitoring and Controlling a CPS System (Actual Hardware)

**Aim:** Write a program to design and develop a user interface for monitoring and controlling a CPS system. In this practical an ESP32 LED web server is built: a web page controls two LEDs.

**Software:** Arduino IDE

**Hardware required:** ESP32 (ESP-WROOM-32) board, micro USB data cable, breadboard, 2 LEDs, 2 resistors (220 ohm), jumper wires, Laptop/PC, a Wi-Fi hotspot (mobile hotspot works).

## Connections
1. Connect the ESP32 to the laptop with the USB data cable.
2. GPIO 12 -> 220 ohm resistor -> anode (long leg) of LED 1; LED 1 cathode -> GND.
3. GPIO 14 -> 220 ohm resistor -> anode (long leg) of LED 2; LED 2 cathode -> GND.

The same connections are also saved separately in this folder as `connections.txt` and `diagram.json`.

## How to run
1. In the code, set WIFI_SSID and WIFI_PASSWORD to your hotspot name and password.
2. Upload the code from Arduino IDE (select the ESP32 board and the right port).
3. Open Serial Monitor at 115200 baud, press EN (reset) and note the IP address printed after Wi-Fi connects.
4. Connect your phone/laptop to the same network and open that IP address in a browser.
5. Use the ON/OFF buttons for GPIO 12 and GPIO 14 and watch the LEDs and the Serial Monitor (requests like /12/on appear there).
