python
import requests

url = 'https://httpbin.org/delete'
response = requests.delete(url)
print(response.status_code)  # Output: 200
print(response.json())       # Output: JSON-innholdet i svaret