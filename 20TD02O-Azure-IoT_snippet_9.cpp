// Arduino-eksempel for å lese fra en temperatursensor og styre en LED
const int sensorPin = A0; // Pin for temperatursensor
const int ledPin = 13;    // Pin for LED

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  float temperature = sensorValue * (5.0 / 1023.0) * 100; // Omregning til grader Celsius
  
  Serial.print("Temperature: ");
  Serial.println(temperature);
  
  if (temperature > 30) { // Hvis temperaturen er over 30 grader
    digitalWrite(ledPin, HIGH); // Slå på LED
  } else {
    digitalWrite(ledPin, LOW); // Slå av LED
  }
  
  delay(1000); // Vent 1 sekund før neste avlesning
}