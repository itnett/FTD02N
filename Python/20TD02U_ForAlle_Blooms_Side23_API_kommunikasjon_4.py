python
import requests

# Få tilgangstoken via OAuth 2.0
token_url = 'https://auth.example.com/oauth/token'
client_id = 'client-id'
client_secret = 'client-secret'
data = {'grant_type': 'client_credentials'}

response = requests.post(token_url, auth=(client_id, client_secret), data=data)
token = response.json().get('access_token')

# Bruk tokenet for å få tilgang til beskyttet ressurs
headers = {'Authorization': f'Bearer {token}'}
api_response = requests.get('https://api.example.com/protected', headers=headers)
print(api_response.json())