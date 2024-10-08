python
   try:
       response = requests.get(url)
       response.raise_for_status()
   except requests.exceptions.HTTPError as err:
       print(f"HTTP error occurred: {err}")
   except Exception as err:
       print(f"Other error occurred: {err}")