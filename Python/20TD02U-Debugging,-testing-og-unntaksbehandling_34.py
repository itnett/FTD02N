python
   def authenticate(username, password):
       return username == "admin" and password == "secret"

   class TestAuthentication(unittest.TestCase):
       def test_authenticate(self):
           self.assertTrue(authenticate("admin", "secret"))
           self.assertFalse(authenticate("user", "wrongpassword"))

   if __name__ == '__main__':
       unittest.main()