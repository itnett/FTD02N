python
# Installere et bibliotek (requests)
# pip install requests

# Bruke requests-biblioteket til å gjøre et HTTP-anrop
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())