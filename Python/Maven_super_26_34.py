python
def les_fil(filnavn):
    try:
        with open(filnavn, "r") as fil:
            return fil.read()
    except FileNotFoundError:
        return "Filen ble ikke funnet."
    except IOError:
        return "En feil oppstod under lesing av filen."

innhold = les_fil("ikke_eksisterende_fil.txt")
print(innhold)  # Utskrift: Filen ble ikke funnet.