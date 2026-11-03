// Exp 4: Sensor data to cloud/web page - ESP32 + Potentiometer web server
// Actual hardware version: set your hotspot SSID/password below, upload,
// open Serial Monitor (115200) for the IP, then open that IP in a browser
// to see the live Potentiometer value on the web page.

#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "YourHotspot";
const char* password = "";

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
  WiFi.begin(ssid, password);
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
