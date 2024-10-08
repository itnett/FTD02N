python
import math

def pytagoras(a=3, b=4):
    """
    Bruker Pytagoras' setning til å finne hypotenusen i en rettvinklet trekant.
    
    Parametere:
    a (int/float): Lengden av den ene kateten (standardverdi 3)
    b (int/float): Lengden av den andre kateten (standardverdi 4)
    
    Returnerer:
    float: Lengden av hypotenusen
    """
    c = math.sqrt(a**2 + b**2)
    return c

# Eksempel på bruk
hypotenus = pytagoras()
print(f'Hypotenusen er: {hypotenus:.2f}')