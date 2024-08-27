python
# ---- 50. Error Handling - Else (continued) ----
try:
    resultat = 10 / 2
except ZeroDivisionError:
    print("Kan ikke dele på null!")
else:
    print(f"Resultatet er {resultat}")

# ---- 51. Custom Exceptions ----
class CustomError(Exception):
    """Egendefinert unntaksklasse for spesifikke feil."""
    pass

try:
    raise CustomError("Dette er en egendefinert feil!")
except CustomError as e:
    print(e)

# ---- 52. Logging ----
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Dette er en informasjonslogg.")

# ---- 53. Assertions ----
assert x == 7, "x burde være 7"

# ---- 54. Classes ----
class Person:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def presentere(self):
        return f"Hei, jeg heter {self.navn} og er {self.alder} år gammel."

# ---- 55. Objects ----
p = Person("Marius", 30)
print(p.presentere())

# ---- 56. Constructors ----
class Bil:
    def __init__(self, merke, modell):
        self.merke = merke
        self.modell = modell

# ---- 57. Instance Methods ----
class Hund:
    def __init__(self, navn):
        self.navn = navn

    def bark(self):
        return f"{self.navn} sier voff!"

# ---- 58. Class Methods ----
class Dyr:
    antall_dyr = 0

    @classmethod
    def legg_til_dyr(cls):
        cls.antall_dyr += 1

# ---- 59. Static Methods ----
class Matematikk:
    @staticmethod
    def addere(x, y):
        return x + y

print(Matematikk.addere(5, 10))

# ---- 60. Inheritance ----
class Katt(Dyr):
    def __init__(self, navn):
        self.navn = navn

# ---- 61. Polymorphism ----
def dyrelyd(dyr):
    print(dyr.bark())

hund = Hund("Fido")
dyrelyd(hund)

# ---- 62. Encapsulation ----
class Konto:
    def __init__(self, saldo):
        self.__saldo = saldo

    def legg_til(self, beløp):
        self.__saldo += beløp
        return self.__saldo

# ---- 63. Abstraction ----
from abc import ABC, abstractmethod

class Transportmiddel(ABC):
    @abstractmethod
    def kjøre(self):
        pass

class Bil(Transportmiddel):
    def kjøre(self):
        print("Bilen kjører.")

bil = Bil()
bil.kjøre()

# ---- 64. Magic Methods ----
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, andre):
        return Punkt(self.x + andre.x, self.y + andre.y)

# ---- 65. Properties ----
class Sirkel:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, verdi):
        if verdi > 0:
            self.__radius = verdi

# ---- 66. Decorators ----
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Funksjonen {func.__name__} ble kalt")
        return func(*args, **kwargs)
    return wrapper

@logger
def si_hei():
    print("Hei!")

si_hei()

# ---- 67. Context Managers ----
with open("example.txt", "w") as file:
    file.write("Dette er en testfil")

# ---- 68. Type Annotations ----
def legg_til(x: int, y: int) -> int:
    return x + y

# ---- 69. Sorted Function ----
tall_liste = [5, 3, 8, 6]
print(sorted(tall_liste))

# ---- 70. Reversed Function ----
for i in reversed(range(5)):
    print(i)

# ---- 71. Range Function ----
for i in range(10):
    print(i)

# ---- 72. Round Function ----
print(round(3.14159, 2))

# ---- 73. Max Function ----
print(max([1, 2, 3, 4]))

# ---- 74. Min Function ----
print(min([1, 2, 3, 4]))

# ---- 75. Sum Function ----
print(sum([1, 2, 3, 4]))

# ---- 76. Any Function ----
print(any([False, False, True]))

# ---- 77. All Function ----
print(all([True, True, True]))

# ---- 78. Isinstance Function ----
print(isinstance(5, int))

# ---- 79. Help Function ----
help(print)

# ---- 80. Modules ----
import math
print(math.sqrt(16))

# ---- 81. Packages ----
import os

# ---- 82. __init__.py ----
# (eksempel krever en Python-pakke struktur med en __init__.py fil)

# ---- 83. import ----
import math

# ---- 84. from ... import ----
from math import sqrt

# ---- 85. as ----
import math as m

# ---- 86. Navnerom ----
# (Eksempel på navnekollisjoner og bruk av moduler for å unngå dem)

# ---- 87. Globale variabler ----
global_var = "Global"

def funksjon():
    global global_var
    global_var = "Endret"

funksjon()
print(global_var)

# ---- 88. Lokale variabler ----
def funksjon():
    lokal_var = "Lokal"
    print(lokal_var)

funksjon()

# ---- 89. LEGB-regelen ----
def funksjon():
    x = "Lokal"
    def indre_funksjon():
        print(x)
    indre_funksjon()

funksjon()

# ---- 90. Unntakshåndtering i funksjoner ----
def del_med_null(x):
    try:
        return x / 0
    except ZeroDivisionError:
        return "Kan ikke dele på null"

print(del_med_null(5))

# ---- 91. Iteratorer ----
class MineTall:
    def __init__(self):
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 10:
            resultat = self.n
            self.n += 1
            return resultat
        else:
            raise StopIteration

for tall in MineTall():
    print(tall)

# ---- 92. iter() ----
my_list = [1, 2, 3]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))

# ---- 93. next() ----
# (Eksempel allerede gitt i forrige konsept)

# ---- 94. StopIteration ----
# (Eksempel allerede gitt i Iterator-konseptet)

# ---- 95. Virtuelle miljøer ----
# (Krever bruk av `venv` kommando i terminalen, ikke egnet for kodesnitt)

# ---- 96. Pip ----
# (Installasjon og bruk av pip kommando i terminal, eks. `pip install requests`)

# ---- 97. Requirements.txt ----
# (Bruk av en requirements.txt fil i et Python prosjekt)

# ---- 98. PyPI ----
# (Bruk av `pip` for å installere pakker fra PyPI)

# ---- 99. Testing ----
import unittest

def legg_til(x, y):
    return x + y

class TestLeggTil(unittest.TestCase):
    def test_legg_til(self):
        self.assertEqual(legg_til(2, 3), 5)

if __name__ == "__main__":
    unittest.main()

# ---- 100. Debugging ----
import pdb; pdb.set_trace()
x = 1
y = 2
print(x + y)