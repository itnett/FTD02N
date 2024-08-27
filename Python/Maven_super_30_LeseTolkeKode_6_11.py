python
import random
import requests
from datetime import datetime

class IoTDevice:
    def __init__(self, name, device_type):
        """
        Initialiserer en IoT-enhet med navn og type.
        """
        self.name = name
        self.device_type = device_type
        self.data = None
        self.timestamp = None
    
    def generate_data(self):
        """
        Generer tilfeldig data basert på enhetstype.
        """
        if self.device_type == "Temperature Sensor":
            self.data = random.uniform(20.0, 30.0)
        elif self.device_type == "Humidity Sensor":
            self.data = random.uniform(30.0, 70.0)
        elif self.device_type == "Pressure Sensor":
            self.data = random.uniform(950.0, 1050.0)
        
        self.timestamp = datetime.now().isoformat()  # Legger til et tidsstempel
        return self.data

    def send_data(self, api_url):
        """
        Send generert data til et API-endepunkt.
        """
        payload = {
            'device': self.name, 
            'type': self.device_type, 
            'data': self.data,
            'timestamp': self.timestamp
        }
        response = requests.post(api_url, json=payload)
        return response.status_code

# Hovedscriptet
def main():
    # Oppretter flere sensorer
    sensors = [
        IoTDevice("TempSensor1", "Temperature Sensor"),
        IoTDevice("HumidSensor1", "Humidity Sensor"),
        IoTDevice("PressureSensor1", "Pressure Sensor")
    ]
    
    api_url = "http://example.com/api/data"  # Simulert API-endepunkt

    for sensor in sensors:
        data = sensor.generate_data()
        print(f"{sensor.name} generated data: {data} {sensor.device_type.split()[0]}")
        
        # Sender data til API
        status = sensor.send_data(api_url)
        if status == 200:
            print(f"Data sent successfully for {sensor.name}!")
        else:
            print(f"Failed to send data for {sensor.name}.")

if __name__ == "__main__":
    main()