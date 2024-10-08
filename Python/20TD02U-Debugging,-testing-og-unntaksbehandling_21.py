python
from unittest.mock import patch, MagicMock
import unittest

# Eksempel: En funksjon som henter data fra en API
def fetch_data_from_api(url):
    import requests
    response = requests.get(url)
    return response.json()

class TestFetchData(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data_from_api(self, mock_get):
        # Konfigurer mockobjektet
        mock_response = MagicMock()
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        url = 'https://api.example.com/data'
        result = fetch_data_from_api(url)

        # Verifiser at mockobjektet ble kalt som forventet
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, {'key': 'value'})

if __name__ == '__main__':
    unittest.main()