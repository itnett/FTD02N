python
     import unittest

     def multiply(a, b):
         return a * b

     class TestIntegration(unittest.TestCase):
         def test_add_and_multiply(self):
             self.assertEqual(multiply(add(2, 3), 2), 10)

     if __name__ == '__main__':
         unittest.main()