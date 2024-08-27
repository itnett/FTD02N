python
   import requests

   url = 'https://api.github.com/user'
   token = 'YOUR_PERSONAL_ACCESS_TOKEN'  # Replace with your GitHub token

   headers = {
       'Authorization': f'Bearer {token}'
   }

   try:
       response = requests.get(url, headers=headers)
       response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
       print('Authenticated GET Response JSON:')
       print(response.json())
   except requests.exceptions.HTTPError as http_err:
       print(f'HTTP error occurred: {http_err}')
   except Exception as err:
       print(f'Other error occurred: {err}')