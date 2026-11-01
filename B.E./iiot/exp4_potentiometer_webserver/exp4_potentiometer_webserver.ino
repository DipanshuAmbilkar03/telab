// Exp 4: Sensor data to cloud/web page - ESP32 + Potentiometer web server
// Wokwi: uses Wokwi-GUEST (open). Real hardware: set your hotspot SSID/password.
// Browser access in Wokwi online: needs IoT Gateway, or just check Serial.
// Real hardware: open printed IP in browser -> shows Potentiometer value.

#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "Wokwi-GUEST";
const char* password = "";
const int WIFI_CHANNEL = 6;

const int potPin = 34;
int potValue = 0;

WebServer server(80);

void handleRoot() {
  String html = "<!DOCTYPE html><html><head><meta http-equiv='refresh' content='2'>";
  html += "<meta name='viewport' content='width=device-width,initial-scale=1'>";
  html += "<style>body{font-family:Arial;text-align:center;margin-top:50px}</style>";
  html += "</head><body><h1>IIoT Sensor Cloud Monitor</h1>";
  html += "<h2>Potentiometer value: " + String(potValue) + "</h2>";
  if (potValue > 2000) html += "<h3 style='color:red'>WARNING: High value!</h3>";
  else html += "<h3 style='color:green'>Status: Normal</h3>";
  html += "</body></html>";
  server.send(200, "text/html", html);
}

void setup() {
  Serial.begin(115200);
  pinMode(potPin, INPUT);

  Serial.print("Connecting to WiFi ");
  Serial.print(ssid);
  WiFi.begin(ssid, password, WIFI_CHANNEL);
  while (WiFi.status() != WL_CONNECTED) {
    delay(200);
    Serial.print(".");
  }
  Serial.println(" Connected!");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/", HTTP_GET, handleRoot);
  server.begin();
  Serial.println("Web server started.");
}

void loop() {
  potValue = analogRead(potPin);
  Serial.println(potValue);
  server.handleClient();
  delay(100);
}
