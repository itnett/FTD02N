python
   import requests

   base_url = 'https://jsonplaceholder.typicode.com/posts'

   # GET request
   response = requests.get(base_url)
   print(f'GET Status Code: {response.status_code}')
   print('GET Response JSON:')
   print(response.json()[:2])  # Print only first 2 items for brevity

   # POST request
   new_post = {
       'title': 'foo',
       'body': 'bar',
       'userId': 1
   }
   response = requests.post(base_url, json=new_post)
   print(f'POST Status Code: {response.status_code}')
   print('POST Response JSON:')
   print(response.json())

   # PUT request
   update_post = {
       'title': 'foo updated',
       'body': 'bar updated',
       'userId': 1
   }
   response = requests.put(f'{base_url}/1', json=update_post)
   print(f'PUT Status Code: {response.status_code}')
   print('PUT Response JSON:')
   print(response.json())

   # DELETE request
   response = requests.delete(f'{base_url}/1')
   print(f'DELETE Status Code: {response.status_code}')
   print('DELETE Response JSON:')
   print(response.json())