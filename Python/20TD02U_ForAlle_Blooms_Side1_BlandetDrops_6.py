python
import requests

response = requests.get('https://api.example.com/users')
if response.status_code == 200:
    users = response.json()   
    for user in users:
        print(user['name'])
else:
    print("Feil ved henting av brukerdata")