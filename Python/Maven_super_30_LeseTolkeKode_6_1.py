python
import random
import requests

class IoTDevice:
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type
        self.data = 0
    
    def generate_data(self):
        # Simulate data generation
        if self.device_type == "Temperature Sensor":
            self.data = random.uniform(20.0, 30.0)
        elif self.device_type == "Humidity Sensor":
            self.data = random.uniform(30.0, 70.0)
        return self.data

    def send_data(self, api_url):
        # Send data to an API endpoint
        payload = {'device': self.name, 'type': self.device_type, 'data': self.data}
        response = requests.post(api_url, json=payload)
        return response.status_code

# Main script
def main():
    sensor = IoTDevice("Sensor1", "Temperature Sensor")
    data = sensor.generate_data()
    print(f"Generated Data: {data} °C")
    
    # Simulate sending data to an API
    api_url = "http://example.com/api/data"
    status = sensor.send_data(api_url)
    
    if status == 200:
        print("Data sent successfully!")
    else:
        print("Failed to send data.")

if __name__ == "__main__":
    main()