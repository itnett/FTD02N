python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # Output: 200
print(response.json())       # Output: JSON-innholdet i svaret