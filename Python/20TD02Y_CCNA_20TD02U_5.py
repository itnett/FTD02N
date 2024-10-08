python
import requests
import json

# Enhetsinformasjon
url = "https://<cisco_device_ip>/restconf/data/ietf-interfaces:interfaces"
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

# Autentisering
auth = ('<username>', '<password>')

# Eksempeldata for oppretting av en ny grensesnitt
payload = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet1",
        "description": "Added via REST API",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(payload), auth=auth, verify=False)

if response.status_code == 201:
    print("Interface created successfully.")
else:
    print(f"Failed to create interface. Status code: {response.status_code}")