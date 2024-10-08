python
import requests

url = 'https://api.example.com/v1/users/1'
data = {
    'name': 'John Doe',
    'email': 'john.doe@example.com'
}

response = requests.put(url, json=data)

if response.status_code == 200:
    print("User updated successfully")
else:
    print(f"Failed to update user: {response.status_code}")