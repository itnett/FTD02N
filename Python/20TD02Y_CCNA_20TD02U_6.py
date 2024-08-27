python
url = "https://<cisco_device_ip>/restconf/data/Cisco-IOS-XE-native:native/policy-map"
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

auth = ('<username>', '<password>')

payload = {
    "Cisco-IOS-XE-policy:policy-map": [
        {
            "name": "QoS-POLICY",
            "class": [
                {
                    "name": "class-default",
                    "bandwidth": {
                        "percent": 30
                    }
                }
            ]
        }
    ]
}

response = requests.put(url, headers=headers, data=json.dumps(payload), auth=auth, verify=False)

if response.status_code == 204:
    print("QoS Policy created successfully.")
else:
    print(f"Failed to create QoS Policy. Status code: {response.status_code}")