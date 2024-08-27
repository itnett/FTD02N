python
import re

# Eksempel på Python-skript for å analysere en MySQL-feillogg
def analysere_feillogg(loggfil):
    med open(loggfil, 'r') as fil:
        linjer = fil.readlines()

    feil_mønster = re.compile(r'ERROR')
    feil_count = 0

    for linje i linjer:
        hvis feil_mønster.search(linje):
            feil_count += 1

    print(f'Antall feil funnet: {feil_count}')

analysere_feillogg('/var/log/mysql/error.log')