#include <AzureIoTHub.h>

  void setup() {
    // Initialiser Azure IoT Hub-tilkobling
  }

  void loop() {
    // Les temperatur fra sensor
    float temperature = readTemperature();

    // Send temperatur til Azure IoT Hub
    sendMessage(temperature);

    delay(1000); // Vent 1 sekund
  }