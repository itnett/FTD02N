python
import unittest

class TestBankKonto(unittest.TestCase):
    def test_innskudd(self):
        konto = BankKonto(100)
        konto.innskudd(50)
        self.assertEqual(konto.vis_saldo(), 150)

    def test_uttak(self):
        konto = BankKonto(100)
        konto.uttak(50)
        self.assertEqual(konto.vis_saldo(), 50)

if __name__ == '__main__':
    unittest.main()