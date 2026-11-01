# Practical 3: Pushbutton and LED with ESP32 (as per IIOT manual)

Aim: To read a pushbutton using ESP32 and switch an LED on and off based on the button state, showing the status on the Serial Monitor.

## Components
- ESP32 development board
- Pushbutton
- LED
- 220 ohm resistor (for LED)
- 10k ohm resistor (pull-down for the button)
- Breadboard and jumper wires

## Wiring
- Pushbutton one leg -> ESP32 3V3
- Pushbutton other leg -> ESP32 GPIO 4
- GPIO 4 -> 10k ohm resistor -> GND (pull-down, so the pin reads LOW when the button is not pressed)
- ESP32 GPIO 12 -> 220 ohm resistor -> LED anode (long leg)
- LED cathode (short leg) -> GND

## Board and upload
- Board: ESP32 Dev Module
- Serial Monitor: 115200

## Expected output
Pressing the button turns the LED on and the Serial Monitor prints "LED ON". Releasing it turns the LED off and prints "LED OFF".
