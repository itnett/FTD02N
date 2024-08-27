#include "DHT.h"

#define DHTPIN 2     // Pin for DHT11-sensor
#define DHTTYPE DHT11   // Definer type DHT-sensor

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Sjekk om avlesningen er vellykket
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
  
  delay(2000); // Vent 2 sekunder før neste avlesning
}