python
import requests
import json

# DNA Center API-endepunkt og autentisering
url = "https://<dnacenter_ip>/dna/intent/api/v1/network-device"
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": "<dnacenter_token>"
}

response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    devices = response.json()
    print("List of network devices:")
    for device in devices['response']:
        print(f"Device ID: {device['id']}, Device Type: {device['type']}")
else:
    print(f"Failed to retrieve devices. Status code: {response.status_code}")