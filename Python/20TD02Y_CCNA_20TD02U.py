python
import requests

url = "https://api.meraki.com/api/v1/organizations/<organization_id>/devices"
headers = {
    "Content-Type": "application/json",
    "X-Cisco-Meraki-API-Key": "<meraki_api_key>"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    devices = response.json()
    print("List of Meraki devices:")
    for device in devices:
        print(f"Device Name: {device['name']}, Model: {device['model']}")
else:
    print(f"Failed to retrieve devices. Status code: {response.status_code}")