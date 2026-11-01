const int buttonPin = 4;     // the pin number of the pushbutton pin
const int ledPin = 12;       // the pin of LED

int buttonState = 0;         // variable for storing the pushbutton status

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(buttonPin, INPUT);  // initialize the pushbutton pin as an input
  pinMode(ledPin, OUTPUT);    // initialize the LED pin as an output
  Serial.println("Hello, ESP32!");
}

void loop() {
  // read the state of the pushbutton value
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    digitalWrite(ledPin, buttonState);
    Serial.println("LED ON");
  } else if (buttonState == LOW) {
    digitalWrite(ledPin, buttonState);
    Serial.println("LED OFF");
  }
  delay(60);
}
