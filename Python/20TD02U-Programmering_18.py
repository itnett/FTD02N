python
# Python - Bruk av requests biblioteket
import requests
response = requests.get("https://api.example.com/data")
print(response.json())