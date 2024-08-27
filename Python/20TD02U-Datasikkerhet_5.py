python
import requests

# Gjør en HTTPS-forespørsel
response = requests.get('https://secureapi.example.com/data')
print(response.json())