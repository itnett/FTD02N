python
import requests

def send_data_to_iot_hub(device_id, data):
    # Example Azure IoT Hub endpoint (replace with real endpoint)
    url = f"https://your-iot-hub.azure-devices.net/devices/{device_id}/messages/events?api-version=2018-06-30"
    
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 204:
        print("Data sent successfully!")
    else:
        print(f"Failed to send data: {response.status_code}")

def main():
    device_id = "MyIoTDevice"
    data = {
        "temperature": 22.5,
        "humidity": 60
    }
    
    send_data_to_iot_hub(device_id, data)

if __name__ == "__main__":
    main()