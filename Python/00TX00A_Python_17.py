python
def regneregler(a=2, b=3):
    """
    Demonstrerer grunnleggende regneregler i algebra.
    
    Parametere:
    a (int/float): Første tall (standardverdi 2)
    b (int/float): Andre tall (standardverdi 3)
    
    Returnerer:
    dict: En ordbok med resultatene av forskjellige regneoperasjoner
    """
    resultater = {
        'addisjon': a + b,
        'subtraksjon': a - b,
        'multiplikasjon': a * b,
        'divisjon': a / b if b != 0 else 'Ikke definert'
    }
    return resultater

# Eksempel på bruk
resultater = regneregler()
for operasjon, resultat i resultater.items():
    print(f'{operasjon.capitalize()}: {resultat}')