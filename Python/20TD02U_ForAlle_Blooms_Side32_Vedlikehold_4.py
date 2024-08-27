python
# Refaktorering av en funksjon for å forbedre lesbarhet og gjenbruk
def beregn_sum(liste):
    return sum(liste)

def beregn_gjennomsnitt(liste):
    return beregn_sum(liste) / len(liste)