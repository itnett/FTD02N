python
# Trinket-kode for Leksjon 6.11: Potenslikninger

import sympy as sp

def los_potenslikning(likning):
    x = sp.symbols('x')
    likning = sp.sympify(likning)
    løsning = sp.solve(likning, x)
    return løsning

# Eksempelbruk
print("Leksjon 6.11: Potenslikninger")
likning = input("Skriv inn potenslikningen (f.eks. 2**x - 16 = 0): ")
løsning = los_potenslikning(likning)
print(f"Løsningen for potenslikningen '{likning}' er: {løsning}")