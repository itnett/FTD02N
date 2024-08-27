python
import requests

def get_data_from_api():
    response = requests.get('https://api.example.com/data')
    if response.status_code == 200:
        return response.json()
    else:
        return None

data = get_data_from_api()
print(data)