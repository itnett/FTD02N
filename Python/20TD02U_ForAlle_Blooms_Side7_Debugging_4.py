python
   import unittest

   def addisjon(a, b):
       return a + b

   class TestMatte(unittest.TestCase):
       def test_addisjon(self):
           self.assertEqual(addisjon(5, 3), 8)
           self.assertEqual(addisjon(-1, 1), 0)

   if __name__ == '__main__':
       unittest.main()