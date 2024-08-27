python
def les_fil(filnavn):
    with open(filnavn, 'r') as fil:
        innhold = fil.read()
    return innhold

def tell_ord(tekst):
    ordliste = tekst.split()
    return len(ordliste)

def skriv_til_fil(filnavn, innhold):
    with open(filnavn, 'w') as fil:
        fil.write(innhold)

# Hovedprogram
tekst = les_fil('input.txt')
antall_ord = tell_ord(tekst)
skriv_til_fil('output.txt', f"Antall ord: {antall_ord}")
print("Ordtelling fullført. Se output.txt for resultat.")