python
# Trinket-kode for Leksjon 6.8: Multiplikasjons- og Divisjonsmetoden

import sympy as sp

def multiplikasjons_divisjonsmetoden(likning1, likning2, faktor):
    x, y = sp.symbols('x y')
    likning1 = sp.sympify(likning1)
    likning2 = sp.sympify(likning2) * faktor
    løsning = sp.solve((likning1, likning2), (x, y))
    return løsning

# Eksempelbruk
print("Leksjon 6.8: Multiplikasjons- og Divisjonsmetoden")
likning1 = input("Skriv inn første likning (f.eks. x + 2y = 8): ")
likning2 = input("Skriv inn andre likning (f.eks. 3x - 2y = 4): ")
faktor = int(input("Skriv inn faktoren for multiplikasjon: "))
løsning = multiplikasjons_divisjonsmetoden(likning1, likning2, faktor)
print(f"Løsningen for systemet er: {løsning}")