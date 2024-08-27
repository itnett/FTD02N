python
   import unittest

   def add(a, b):
       return a + b

   class TestAddFunction(unittest.TestCase):
       def test_add(self):
           self.assertEqual(add(3, 4), 7)
           self.assertEqual(add(-1, 1), 0)

   if __name__ == '__main__':
       unittest.main()