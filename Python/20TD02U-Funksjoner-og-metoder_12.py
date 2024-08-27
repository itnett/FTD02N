python
     import requests

     def fetch_data(url):
         response = requests.get(url)
         return response.json()

     data = fetch_data('https://api.example.com/data')
     print(data)