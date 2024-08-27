python
   from unittest.mock import MagicMock
   import unittest

   class Database:
       def fetch_data(self):
           pass  # This would normally interact with a real database

   class DataService:
       def __init__(self, db: Database):
           self.db = db

       def get_data(self):
           return self.db.fetch_data()

   class TestDataService(unittest.TestCase):
       def test_get_data(self):
           mock_db = MagicMock()
           mock_db.fetch_data.return_value = "mocked data"
           service = DataService(mock_db)

           result = service.get_data()
           self.assertEqual(result, "mocked data")

   if __name__ == '__main__':
       unittest.main()