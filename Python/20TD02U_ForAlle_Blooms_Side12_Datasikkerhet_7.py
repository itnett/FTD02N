python
import requests

response = requests.get('https://sikker-website.com', verify=True)
print(response.content)