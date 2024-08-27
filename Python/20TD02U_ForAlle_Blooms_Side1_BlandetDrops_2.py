python
import requests

response = requests.get('https://www.example.com')
if response.status_code == 200:
    print(response.text) 
else:
    print("Feil ved henting av nettsiden")