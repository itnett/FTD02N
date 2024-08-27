python
def les_fil(filnavn):
    try:
        with open(filnavn, "r") as f:
            innhold = f.read()
            return innhold
    except FileNotFoundError:
        print(f"Fant ikke filen: {filnavn}")
        return None
    except PermissionError:
        print(f"Ingen tilgang til filen: {filnavn}")
        return None