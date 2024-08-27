python
import requests

url = 'https://api.example.com/v1/users'
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    print(users)
else:
    print(f"Failed to retrieve data: {response.status_code}")