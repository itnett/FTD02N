python
import unittest

def addisjon(a, b):
    return a + b

class TestAddisjon(unittest.TestCase):
    def test_addisjon(self):
        self.assertEqual(addisjon(2, 3), 5)
        self.assertEqual(addisjon(-1, 1), 0)
        self.assertEqual(addisjon(0, 0), 0)

if __name__ == "__main__":
    unittest.main()