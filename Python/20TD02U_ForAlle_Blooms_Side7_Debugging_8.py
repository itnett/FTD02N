python
class MinEgendefinertFeil(Exception):
    pass

def sjekk_verdi(verdi):
    if verdi < 0:
        raise MinEgendefinertFeil("Verdi kan ikke være negativ!")
    return True

try:
    sjekk_verdi(-1)
except MinEgendefinertFeil as e:
    print(e)  # Utdata: Verdi kan ikke være negativ!