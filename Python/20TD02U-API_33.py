python
import requests

url = 'https://api.example.com/data'
headers = {'Authorization': 'Bearer YOUR_API_KEY'}
response = requests.get(url, headers=headers)
print(response.status_code)  # Output: 200 (hvis nøkkelen er gyldig)
print(response.json())       # Output: JSON-innholdet i svaret