python
import requests

url = 'https://www.example.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} er tilgjengelig.")
    else:
        print(f"{url} returnerte statuskode {response.status_code}.")
except requests.exceptions.RequestException as e:
    print(f"Kunne ikke nå {url}: {e}")