python
   import requests

   def test_api_response():
       response = requests.get('https://api.example.com/data')
       assert response.status_code == 200
       assert 'expected_key' in response.json()