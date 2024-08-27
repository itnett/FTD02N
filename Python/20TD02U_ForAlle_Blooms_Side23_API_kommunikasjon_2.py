python
import requests

url = 'https://api.example.com/graphql'
query = """
{
  user(id: 1) {
    name
    email
    friends {
      name
    }
  }
}
"""

response = requests.post(url, json={'query': query})
if response.status_code == 200:
    print(response.json())
else:
    print('Forespørsel feilet')