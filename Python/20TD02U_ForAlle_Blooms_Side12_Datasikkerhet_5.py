python
import requests

url = 'https://api.eksempel.com/data'
headers = {
    'Authorization': 'Bearer TOKEN_HER',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.json())
else:
    print("Feil:", response.status_code)