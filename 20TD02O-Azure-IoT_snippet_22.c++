const int sensorPin = 2;  // Pin for bevegelsessensor
const int relayPin = 7;   // Pin for relé

void setup() {
  pinMode(sensorPin, INPUT);
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);       // For seriell kommunikasjon (valgfritt)
}

void loop() {
  int sensorValue = digitalRead(sensorPin);
  if (sensorValue == HIGH) {
    Serial.println("Bevegelse oppdaget!");
    digitalWrite(relayPin, HIGH);  // Slå på reléet (og dermed lyspæren)
    delay(5000);                  // Hold lyset på i 5 sekunder
    digitalWrite(relayPin, LOW);   // Slå av reléet (og dermed lyspæren)
  }
}