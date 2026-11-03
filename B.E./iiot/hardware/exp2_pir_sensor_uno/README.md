# Experiment 2: Interfacing PIR Sensor with Arduino (Actual Hardware)

**Aim:** Write an Arduino / Raspberry Pi program for interfacing with PIR sensor.

**Software:** Arduino IDE (the manual also lists Tinkercad for simulation)

**Hardware required:** Arduino Uno, PIR motion sensor, LED, resistor (220 ohm), breadboard, jumper wires, Laptop/PC.

## Connections
1. PIR sensor GND pin -> GND of Arduino.
2. PIR sensor VCC (power) pin -> 5V of Arduino.
3. PIR sensor OUT (signal) pin -> pin 2 of Arduino.
4. LED anode (long leg) -> pin 13 of Arduino through a 220 ohm resistor.
5. LED cathode (short leg) -> GND of Arduino.

The same connections are also saved separately in this folder as `connections.txt` and `diagram.json`.

## How to run
1. Open the .ino file in Arduino IDE, select Arduino Uno and the right port.
2. Upload the code.
3. Open Serial Monitor at 9600 baud and wave a hand in front of the PIR sensor.

## Expected output
When motion is sensed, the LED turns ON and the Serial Monitor prints "Motion detected!". When there is no motion, the LED turns OFF and it prints "No motion detected."
