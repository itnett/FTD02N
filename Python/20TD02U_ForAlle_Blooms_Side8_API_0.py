python
   import requests

   response = requests.get('https://api.example.com/data')
   if response.status_code == 200:
       data = response.json()
       print(data)