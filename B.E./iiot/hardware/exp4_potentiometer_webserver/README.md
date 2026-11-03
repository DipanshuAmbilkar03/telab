# Experiment 4: Sending Sensor Data to the Cloud / Web Page (Actual Hardware)

**Aim:** Write a program for sending sensor data to the cloud and displaying it on a web page. The ESP32 runs a web server that shows the live potentiometer value on a web page.

**Software:** Arduino IDE (libraries: WiFi, WebServer)

**Hardware required:** ESP32 (ESP-WROOM-32) board, micro USB data cable, breadboard, Potentiometer 10K, male-to-female jumper wires, Laptop/PC, a Wi-Fi hotspot.

## Connections
1. Connect the ESP32 to the laptop with the USB data cable.
2. Potentiometer middle pin (signal) -> GPIO 34 of ESP32.
3. Potentiometer one side pin (red) -> 3.3V of ESP32.
4. Potentiometer other side pin (orange) -> GND of ESP32.

## How to run
1. In the code, set ssid and password to your hotspot name and password.
2. Upload the code from Arduino IDE (select the ESP32 board and the right port).
3. Open Serial Monitor at 115200 baud and note the IP address printed after Wi-Fi connects.
4. Open that IP address in a browser on the same network.

## Expected output
The web page shows the current reading, for example "Potentiometer value: 2233", and it updates as you rotate the potentiometer.
