python
   import requests

   def fetch_data(url):
       try:
           response = requests.get(url)
           response.raise_for_status()
           return response.json()
       except requests.exceptions.HTTPError as http_err:
           return f"HTTP error occurred: {http_err}"
       except Exception as err:
           return f"Other error occurred: {err}"

   print(fetch_data('https://api.example.com/data'))