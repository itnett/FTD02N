python
   import requests

   url = 'https://api.github.com'
   response = requests.get(url)

   print(f'Status Code: {response.status_code}')
   print('Response JSON:')
   print(response.json())