python
class Bankkonto:
    def __init__(self, saldo):
        self.__saldo = saldo  # Privat attributt

    def innskudd(self, beløp):
        self.__saldo += beløp

    def uttak(self, beløp):
        if beløp <= self.__saldo:
            self.__saldo -= beløp
        else:
            print("Utilstrekkelige midler.")