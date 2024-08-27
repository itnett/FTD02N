python
import requests

# Eksempel på GET-forespørsel
response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()
    print(data)

# Eksempel på POST-forespørsel
payload = {'name': 'John', 'age': 30}
response = requests.post('https://api.example.com/users', json=payload)
if response.status_code == 201:
    print('Ressurs opprettet')