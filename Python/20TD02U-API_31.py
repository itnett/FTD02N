python
import requests

url = 'https://httpbin.org/put'
data = {'name': 'Alice', 'age': 26}
response = requests.put(url, json=data)
print(response.status_code)  # Output: 200
print(response.json())       # Output: JSON-innholdet i svaret