// Arduino-eksempel for å styre en DC-motor med et relé
const int relayPin = 7; // Pin for relé

void setup() {
  pinMode(relayPin, OUTPUT);
}

void loop() {
  digitalWrite(relayPin, HIGH); // Slå på motor
  delay(5000); // Kjør motoren i 5 sekunder
  digitalWrite(relayPin, LOW);  // Slå av motor
  delay(5000); // Vent i 5 sekunder før neste syklus
}