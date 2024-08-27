python
import requests

# Hente alle personer
response = requests.get('http://localhost:5000/personer')
if response.status_code == 200:
    personer = response.json()
    print(personer)

# Legge til en ny person
ny_person = {"id": 3, "navn": "Charlie", "alder": 22}
response = requests.post('http://localhost:5000/personer', json=ny_person)
if response.status_code == 201:
    print("Ny person lagt til:", response.json())

# Oppdatere en person
oppdatert_person = {"navn": "Charlie", "alder": 23}
response = requests.put('http://localhost:5000/personer/3', json=oppdatert_person)
if response.status_code == 200:
    print("Person oppdatert:", response.json())

# Slette en person
response = requests.delete('http://localhost:5000/personer/3')
if response.status_code == 204:
    print("Person slettet.")