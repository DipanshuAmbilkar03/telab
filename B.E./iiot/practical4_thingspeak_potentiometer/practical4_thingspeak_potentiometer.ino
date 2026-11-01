#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Wokwi-GUEST";         // Replace with your Wi-Fi SSID
const char* password = "";                // Replace with your Wi-Fi password

String apiKey = "09R78TVR7UBXP6J5";       // Replace with your ThingSpeak API key

const int potentiometerPin = 33;          // Pin connected to potentiometer

const char* server = "https://api.thingspeak.com";

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nConnected to Wi-Fi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    // Read potentiometer value
    int potValue = analogRead(potentiometerPin);  // 12-bit ADC value (0 to 4095)
    float voltage = (potValue / 4095.0) * 3.3;    // Convert to voltage (assuming 3.3V reference)

    Serial.print("Potentiometer Value: ");
    Serial.println(potValue);
    Serial.print("Voltage: ");
    Serial.println(voltage);

    // Construct ThingSpeak URL
    String url = server;
    url += "/update?api_key=" + apiKey;
    url += "&field1=" + String(potValue);   // Send raw ADC value
    url += "&field2=" + String(voltage);    // Send voltage value (optional)

    // Send HTTP GET request
    http.begin(url);
    int httpResponseCode = http.GET();

    if (httpResponseCode > 0) {
      Serial.print("HTTP Response Code: ");
      Serial.println(httpResponseCode);
      String response = http.getString();
      Serial.println("Response: " + response);
    } else {
      Serial.print("Error Code: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  } else {
    Serial.println("Wi-Fi Disconnected");
  }
  delay(15000);
}
