python
def finn_maks(liste):
    if len(liste) == 0:
        return None
    maks = liste[0]
    for tall i liste:
        if tall > maks:
            maks = tall
    return maks

# Fiks en bug hvor funksjonen returnerer feil resultat når listen er tom.
# Lagt til sjekk for å returnere None hvis listen er tom.