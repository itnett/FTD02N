const int relayPin = 7; // Pinne tilkoblet reléet

void setup() {
  pinMode(relayPin, OUTPUT); // Sett relépinnen som utgang
}

void loop() {
  digitalWrite(relayPin, HIGH); // Slå på reléet (og enheten det kontrollerer)
  delay(5000); // Vent 5 sekunder
  digitalWrite(relayPin, LOW); // Slå av reléet (og enheten det kontrollerer)
  delay(5000); // Vent 5 sekunder
}