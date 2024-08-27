python
import requests

# Gjør en GET-forespørsel
response = requests.get("https://api.github.com")

# Konverter svar til JSON
data = response.json()
print(data)