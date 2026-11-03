# IIOT - Computer Laboratory II (417526)

Lab manual: *Lab Manual - Computer Laboratory II: Industrial Internet of Things (417526), BE (AI&DS), ADYPSOE* (Course Coordinator: Prof. Sandeep Kumar). A copy of the manual PDF is in `manuals/IIOT_Lab_Manual.pdf`.

Every experiment is kept in **two versions**:

- **`wokwi/`** - simulation version: Arduino sketch (.ino) + `diagram.json` (the Wokwi connections). Import the folder into Wokwi to run it.
- **`hardware/`** - actual hardware version: the same code (Wi-Fi versions point at your own hotspot) + a README with the manual's hardware list and step-by-step connections.

## Experiment list (as per the manual)

| No | Experiment | Wokwi | Hardware |
|----|------------|-------|----------|
| 1 | Alert message on potentiometer threshold - ESP32, pot on GPIO 34, prints "warning" above 2000 | exp1_potentiometer_alert | exp1_potentiometer_alert |
| 2 | PIR sensor interfacing - Arduino Uno, PIR OUT on pin 2, LED on pin 13 | exp2_pir_sensor_uno | exp2_pir_sensor_uno |
| 3 | User interface for monitoring and controlling a CPS system - ESP32 LED web server, LEDs on GPIO 12 and 14 | exp3_led_webserver | exp3_led_webserver |
| 4 | Sensor data to the cloud / web page - ESP32 web server showing the potentiometer value (GPIO 34) | exp4_potentiometer_webserver | exp4_potentiometer_webserver |
| 5 | Industrial data analysis - Farm Temperature and Humidity in Excel (Python version of the same steps included) | exp5_data_analysis_excel | exp5_data_analysis_excel |

Experiment 5 has no circuit; it is an Excel data-analysis practical, so both trees carry the same data, script and graphs.

## Arduino IDE setup (ESP32 experiments)
1. Arduino IDE > Preferences > Additional boards manager URLs: add the ESP32 URL from Espressif.
2. Tools > Board > Boards Manager: install "esp32 by Espressif Systems".
3. Select your ESP32 board and the correct COM port (install the CH340G driver if the port does not appear).
