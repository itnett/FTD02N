python
def les_fil(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            innhold = fil.read()
            return innhold
    except FileNotFoundError:
        print(f"Feil: Filen '{filnavn}' ble ikke funnet.")
        return None

filinnhold = les_fil("min_fil.txt")
if filinnhold:
    print(filinnhold)