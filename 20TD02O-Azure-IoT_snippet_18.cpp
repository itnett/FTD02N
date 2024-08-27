const int pirPin = 2; // Pinne tilkoblet PIR-sensoren
const int ledPin = 13; // Pinne tilkoblet LED

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int pirState = digitalRead(pirPin);

  if (pirState == HIGH) {
    digitalWrite(ledPin, HIGH); // Slå på LED
    Serial.println("Motion detected!");
  } else {
    digitalWrite(ledPin, LOW); // Slå av LED
    Serial.println("No motion");
  }

  delay(1000); // Vent 1 sekund før neste avlesning
}