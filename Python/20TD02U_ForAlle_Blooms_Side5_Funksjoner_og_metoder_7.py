python
class BankKonto:
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def innskudd(self, beløp):
        self.saldo += beløp
    
    def uttak(self, beløp):
        if beløp <= self.saldo:
            self.saldo -= beløp
        else:
            print("Ikke nok saldo!")