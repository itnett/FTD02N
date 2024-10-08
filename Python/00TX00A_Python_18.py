python
def brok_prosent(brok_numer=1, brok_denom=2):
    """
    Demonstrerer omregning fra brøk til prosent.
    
    Parametere:
    brok_numer (int/float): Teller (standardverdi 1)
    brok_denom (int/float): Nevner (standardverdi 2)
    
    Returnerer:
    float: Prosentverdien av brøken
    """
    prosent = (brok_numer / brok_denom) * 100
    return prosent

# Eksempel på bruk
prosent = brok_prosent()
print(f'Brøk til prosent: {prosent:.2f}%')