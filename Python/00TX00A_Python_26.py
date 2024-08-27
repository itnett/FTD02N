python
def analyze_payment_ability_and_capital(ne = 30000):
    """
    Analyserer bedriftens betalingsevne og kapitalbehov.

    Parametere:
    ne (int/float): Nettoeksponering (standardverdi 30000)

    Returnerer:
    dict: En ordbok med analyse av betalingsevne og kapitalbehov
    """
    likviditetsgrad1 = 2.18  # Eksempelverdi
    likviditetsgrad2 = 2.16  # Eksempelverdi

    if likviditetsgrad1 >= 2 and likviditetsgrad2 >= 1.5:
        likviditet = "Bra"
    else:
        likviditet = "Dårlig"

    kapitalbehov = ne  # Enkelt eksempel på kapitalbehov

    return {'likviditet': likviditet, 'kapitalbehov': kapitalbehov}

# Eksempel på bruk
analyse = analyze_payment_ability_and_capital()
print(analyse)