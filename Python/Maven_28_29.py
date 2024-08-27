python
   import unittest

   class TestTransaksjon(unittest.TestCase):
       def test_transaksjon(self):
           t = Transaksjon('2024-09-01', 'Bankkonto', 10000, 'Debet')
           self.assertEqual(t.belop, 10000)

   if __name__ == '__main__':
       unittest.main()