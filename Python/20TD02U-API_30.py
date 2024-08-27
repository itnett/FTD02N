python
import requests

url = 'https://httpbin.org/post'
data = {'name': 'Alice', 'age': 25}
response = requests.post(url, json=data)
print(response.status_code)  # Output: 200
print(response.json())       # Output: JSON-innholdet i svaret