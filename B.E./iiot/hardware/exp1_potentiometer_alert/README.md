# Experiment 1: Alert Message using Potentiometer (Actual Hardware)

**Aim:** Write a program for sending alert messages to the user for controlling and interacting with your environment.

**Software:** Arduino IDE

**Hardware required:** ESP32 (ESP-WROOM-32) board, micro USB data cable, breadboard, Potentiometer 10K, male-to-female jumper wires, Laptop/PC.

## Connections
1. Connect the ESP32 to the laptop with the USB data cable (insert straight, blue light glows).
2. Place the potentiometer on the breadboard.
3. Potentiometer middle pin (signal) -> GPIO 34 of ESP32.
4. Potentiometer one side pin (red) -> 3.3V of ESP32.
5. Potentiometer other side pin (orange) -> GND of ESP32.

## How to run
1. Open the .ino file in Arduino IDE, select your ESP32 board.
2. Select the right port in Tools > Port (COM3 or COM4; install the CH340G driver if the port does not show).
3. Upload the code, press the ESP32 reset (EN) button.
4. Open Serial Monitor at 115200 baud and rotate the potentiometer.

## Expected output
Values change between 0 and 4095. When the value crosses 2000, the Serial Monitor also prints "warning".
