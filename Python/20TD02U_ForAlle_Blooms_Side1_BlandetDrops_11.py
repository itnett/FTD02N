python
import requests

response = requests.post('https://api.example.com/orders', json={'produkt_id': 123, 'antall': 2})

if response.status_code == 201:  # Created
    order_id = response.json()['id']
    print("Ordre opprettet med ID:", order_id)
else:
    print("Feil ved opprettelse av ordre:", response.text)