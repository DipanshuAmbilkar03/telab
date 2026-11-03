# IIOT experiment 2 - Wokwi ESP32, STM32, Arduino Simulator

Wokwi project: https://wokwi.com/projects/477781285471687681

## Files
- sketch.ino
- diagram.json

## Parts (from diagram)
- wokwi-arduino-uno (id: uno)
- wokwi-pir-motion-sensor (id: pir1)
- wokwi-led (id: led1)

## Wiring (connections from diagram.json)
- uno:2 -> pir1:OUT [green]
- uno:5V -> pir1:VCC [red]
- uno:GND.2 -> pir1:GND [black]
- uno:13 -> led1:A [green]
- led1:C -> uno:GND.1 [black]
