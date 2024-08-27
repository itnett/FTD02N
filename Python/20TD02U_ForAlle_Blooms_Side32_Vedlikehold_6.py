python
import unittest

class TestApplikasjon(unittest.TestCase):
    def test_beregn_sum(self):
        self.assertEqual(beregn_sum([1, 2, 3]), 6)
    
    def test_beregn_gjennomsnitt(self):
        self.assertEqual(beregn_gjennomsnitt([2, 4, 6]), 4)
        self.assertIsNone(beregn_gjennomsnitt([]))

if __name__ == '__main__':
    unittest.main()