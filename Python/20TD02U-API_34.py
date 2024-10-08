python
import requests

url = 'https://api.example.com/data'
try:
    response = requests.get(url)
    response.raise_for_status()  # Kaster en feil hvis statuskoden ikke er 200
    data = response.json()
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')