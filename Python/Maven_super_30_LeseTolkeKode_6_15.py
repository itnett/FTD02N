python
import requests
import json

def send_data_to_iot_hub(device_id, data, api_key):
    """
    Sender data til en IoT-hub med autentisering.
    """
    url = f"https://your-iot-hub.azure-devices.net/devices/{device_id}/messages/events?api-version=2018-06-30"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Hever feil hvis statuskoden indikerer feil
        print("Data sent successfully!")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def main():
    device_id = "MyIoTDevice"
    api_key = "your_api_key_here"
    data = {
        "temperature": 22.5,
        "humidity": 60
    }
    
    send_data_to_iot_hub(device_id, data, api_key)

if __name__ == "__main__":
    main()