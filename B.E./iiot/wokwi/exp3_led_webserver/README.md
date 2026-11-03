# IIOT experiment 3

Wokwi project: https://wokwi.com/projects/477781902013608961

Exp 3: CPS monitoring/control UI - ESP32 LED Web Server (GPIO 12, 14). The ESP32 hosts a web page to switch two LEDs on and off. On Wokwi it connects to "Wokwi-GUEST" (open network). On real hardware, change WIFI_SSID and WIFI_PASSWORD in the code to your own network.

## Files
- sketch.ino
- diagram.json

## Parts (from diagram)
- board-esp32-devkit-c-v4 (id: esp)
- wokwi-led (id: led1)
- wokwi-resistor (id: r1)
- wokwi-led (id: led2)
- wokwi-resistor (id: r2)

## Wiring (connections from diagram.json)
- esp:TX -> $serialMonitor:RX
- esp:RX -> $serialMonitor:TX
- esp:12 -> r1:2 [green]
- r1:1 -> led1:A [green]
- esp:14 -> r2:2 [yellow]
- r2:1 -> led2:A [yellow]
- led2:C -> esp:GND.1 [black]
- led1:C -> esp:GND.1 [black]

In short: GPIO 12 -> resistor -> LED1 anode, LED1 cathode -> GND. GPIO 14 -> resistor -> LED2 anode, LED2 cathode -> GND.
