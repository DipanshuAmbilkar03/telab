// Exp 3: CPS monitoring/control UI - ESP32 LED Web Server (GPIO 12, 14)
// Wokwi: connect to "Wokwi-GUEST" (open network, channel 6)
// Real hardware: change WIFI_SSID / WIFI_PASSWORD to your mobile hotspot
// Wokwi browser access: needs Wokwi IoT Gateway (F1 > Enable Private Gateway),
// OR just watch Serial Monitor output. Real hardware: open Serial IP in browser.

#include <WiFi.h>
#include <WebServer.h>

#define WIFI_SSID "Wokwi-GUEST"
#define WIFI_PASSWORD ""
#define WIFI_CHANNEL 6

const int LED1 = 12;
const int LED2 = 14;
bool led1State = false;
bool led2State = false;

WebServer server(80);

String htmlPage() {
  String html = "<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width,initial-scale=1'>";
  html += "<style>body{font-family:Arial;text-align:center;margin-top:40px} .btn{display:inline-block;padding:12px 30px;margin:8px;font-size:18px;text-decoration:none;border-radius:8px} .on{background:#28a745;color:#fff} .off{background:#dc3545;color:#fff}</style>";
  html += "</head><body><h1>IIoT CPS Control Panel</h1>";
  html += "<h2>GPIO 12: " + String(led1State ? "ON" : "OFF") + "</h2>";
  html += "<a class='btn on' href='/12/on'>12 ON</a><a class='btn off' href='/12/off'>12 OFF</a>";
  html += "<h2>GPIO 14: " + String(led2State ? "ON" : "OFF") + "</h2>";
  html += "<a class='btn on' href='/14/on'>14 ON</a><a class='btn off' href='/14/off'>14 OFF</a>";
  html += "</body></html>";
  return html;
}

void handleRoot() { server.send(200, "text/html", htmlPage()); }

void setup() {
  Serial.begin(115200);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);

  Serial.print("Connecting to WiFi ");
  Serial.print(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD, WIFI_CHANNEL);
  while (WiFi.status() != WL_CONNECTED) {
    delay(200);
    Serial.print(".");
  }
  Serial.println(" Connected!");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.on("/12/on", []() { led1State = true; digitalWrite(LED1, HIGH); Serial.println("GET /12/on"); server.send(200, "text/html", htmlPage()); });
  server.on("/12/off", []() { led1State = false; digitalWrite(LED1, LOW); Serial.println("GET /12/off"); server.send(200, "text/html", htmlPage()); });
  server.on("/14/on", []() { led2State = true; digitalWrite(LED2, HIGH); Serial.println("GET /14/on"); server.send(200, "text/html", htmlPage()); });
  server.on("/14/off", []() { led2State = false; digitalWrite(LED2, LOW); Serial.println("GET /14/off"); server.send(200, "text/html", htmlPage()); });
  server.begin();
  Serial.println("Web server started. Open the IP above in browser.");
}

void loop() {
  server.handleClient();
  delay(10);
}
