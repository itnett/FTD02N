python
# Legg til en funksjon som finner gjennomsnittet av en liste
def beregn_gjennomsnitt(liste):
    if len(liste) == 0:
        return None
    return sum(liste) / len(liste)