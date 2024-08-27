python
brukertilgang = {
    "admin": ["lese", "skrive", "kjøre"],
    "bruker1": ["lese"],
    "bruker2": ["lese", "skrive"],
}

def sjekk_tilgang(brukernavn, handling):
    if brukernavn in brukertilgang:
        if handling in brukertilgang[brukernavn]:
            return True
    return False

if sjekk_tilgang("admin", "kjøre"):
    print("Handlingen er tillatt.")
else:
    print("Handlingen er ikke tillatt.")