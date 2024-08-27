python
try:
    with open('ikke_eksisterende_fil.txt', 'r') as fil:
        innhold = fil.read()
except FileNotFoundError:
    print("Filen ble ikke funnet.")
except IOError:
    print("En feil oppstod under lesing av filen.")