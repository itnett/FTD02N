#include <ESP8266WiFi.h>
      #include <DHT.h>

      #define DHTPIN 2
      #define DHTTYPE DHT11
      DHT dht(DHTPIN, DHTTYPE);

      const char* ssid = "YourSSID";
      const char* password = "YourPassword";

      void setup() {
          Serial.begin(115200);
          WiFi.begin(ssid, password);
          while (WiFi.status() != WL_CONNECTED) {
              delay(500);
              Serial.print(".");
          }
          dht.begin();
      }

      void loop() {
          float h = dht.readHumidity();
          float t = dht.readTemperature();
          Serial.println("Temperature: " + String(t) + "C");
          delay(2000);
      }