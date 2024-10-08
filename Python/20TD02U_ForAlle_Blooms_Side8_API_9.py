python
   from unittest.mock import patch
   import requests

   @patch('requests.get')
   def test_api_with_mock(mock_get):
       mock_get.return_value.status_code = 200
       mock_get.return_value.json.return_value = {'key': 'value'}

       response = requests.get('https://api.example.com/data')
       assert response.status_code == 200
       assert response.json() == {'key': 'value'}