python
   import requests

   # Last opp en fil til en API
   url = 'https://example.com/upload'
   files = {'file': open('example.txt', 'rb')}
   response = requests.post(url, files=files)
   print(response.status_code)