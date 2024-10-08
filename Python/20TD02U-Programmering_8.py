python
# Unntaksbehandling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Feil: {e}")

# Enhetstesting
import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 4), 7)

if __name__ == '__main__':
    unittest.main()