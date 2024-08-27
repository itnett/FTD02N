void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Sett den innebygde LED-pinnen som utgang
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Slå på LED
  delay(1000); // Vent 1 sekund
  digitalWrite(LED_BUILTIN, LOW); // Slå av LED
  delay(1000); // Vent 1 sekund
}