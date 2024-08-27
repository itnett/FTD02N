#include "DHT.h"

#define DHTPIN 2       // Pin for DHT11-sensor
#define DHTTYPE DHT11  // DHT11-sensor
#define RELAY_PIN 7    // Pin for relé

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" *C");

  // Kontroller vifte basert på temperatur
  if (temperature > 25) {
    digitalWrite(RELAY_PIN, HIGH); // Slå på vifte
  } else {
    digitalWrite(RELAY_PIN, LOW);  // Slå av vifte
  }

  delay(2000); // Vent 2 sekunder før neste avlesning
}