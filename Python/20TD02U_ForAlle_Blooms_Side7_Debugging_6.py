python
def test_addisjon():
    assert addisjon(5, 3) == 8  # Test som vil feile fordi addisjon() ikke er definert

def addisjon(a, b):
    return a + b  # Skriv koden for å få testen til å passere

# Refaktorering (hvis nødvendig) uten å bryte testen