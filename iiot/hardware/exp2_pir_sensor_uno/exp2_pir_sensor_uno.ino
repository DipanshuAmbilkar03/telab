// Exp 2: PIR sensor interfacing with Arduino Uno
// Hardware: Arduino Uno + PIR sensor + LED
// Wokwi + Real hardware compatible

int pirPin = 2;   // PIR OUT connected to D2
int ledPin = 13;  // LED connected to D13

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int motionState = digitalRead(pirPin);

  if (motionState == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Motion detected!");
    delay(1000);
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("No motion detected.");
    delay(1000);
  }
}
