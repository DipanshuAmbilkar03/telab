# exp 4 iiot - Wokwi ESP32, STM32, Arduino Simulator

Wokwi project: https://wokwi.com/projects/478018508734768129

## Files
- sketch.ino
- diagram.json

## Parts (from diagram)
- board-esp32-devkit-c-v4 (id: esp)
- wokwi-potentiometer (id: pot1)

## Wiring (connections from diagram.json)
- esp:TX -> $serialMonitor:RX
- esp:RX -> $serialMonitor:TX
- esp:34 -> pot1:SIG [green]
- esp:3V3 -> pot1:VCC [red]
- esp:GND.1 -> pot1:GND [black]
