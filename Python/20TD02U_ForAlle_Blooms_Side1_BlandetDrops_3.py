python
def beregn_gjennomsnitt(tall_liste):
    """Beregner gjennomsnittet av en liste med tall."""
    if not tall_liste:  # Sjekk for tom liste
        return None
    return sum(tall_liste) / len(tall_liste)

mine_tall = [1, 5, 3, 8, 2]
gjennomsnitt = beregn_gjennomsnitt(mine_tall)
if gjennomsnitt:
    print