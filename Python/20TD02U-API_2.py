python
import requests

url = 'https://api.example.com/v1/users'
data = {
    'name': 'John Doe',
    'email': 'john.doe@example.com'
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("User created successfully")
else:
    print(f"Failed to create user: {response.status_code}")