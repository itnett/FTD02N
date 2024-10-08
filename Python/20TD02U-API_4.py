python
import requests

url = 'https://api.example.com/v1/users/1'
response = requests.delete(url)

if response.status_code == 204:
    print("User deleted successfully")
else:
    print(f"Failed to delete user: {response.status_code}")