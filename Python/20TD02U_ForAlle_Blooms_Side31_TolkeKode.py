python
# Evaluer denne funksjonen for kodekvalitet og ytelse
def finn_største(liste):
    if len(liste) == 0:
        return None
    største = liste[0]
    for tall i liste:
        if tall > største:
            største = tall
    return største

# Evaluering: Funksjonen er korrekt og returnerer det største tallet i listen. 
# Imidlertid kunne man også bruke Python's innebygde max(liste) for å gjøre koden kortere og potensielt raskere.