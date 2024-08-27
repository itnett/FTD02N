python
import requests  # Importerer requests-biblioteket som brukes til å gjøre HTTP-forespørsler
import math  # Importerer math-biblioteket som gir tilgang til matematiske funksjoner
from bs4 import BeautifulSoup  # Importerer BeautifulSoup for å analysere HTML-innhold

def get_grade(url):
    """
    Henter GitHub-aktiviteten og beregner en "karakter" basert på bidrag fra brukeren.

    Parameter:
    url (str): URL til GitHub-brukerens bidragsside.

    Returnerer:
    str: Brukerens GitHub-karakter basert på beregningslogikken.
    """
    # Sender en GET-forespørsel til GitHub-brukerens bidragsside
    r = requests.get(url)

    # Bruker BeautifulSoup til å analysere HTML-innholdet i GitHub-siden
    soup = BeautifulSoup(r.content, 'html.parser')

    # Finner alle elementer med taggen 'rect' som representerer bidrag i GitHub-heatmap
    rects = soup.find_all('rect')

    total_contributions = 0  # Initialiserer antall totale bidrag

    # Itererer gjennom alle 'rect' elementene
    for rect in rects:
        # Henter attributtet 'data-count' som angir antall bidrag på en spesifikk dag
        count = int(rect['data-count'])
        total_contributions += count  # Legger til antall bidrag i den totale summen

    # Beregner en score basert på totale bidrag
    score = math.log(total_contributions + 1)  # Legger til 1 for å unngå log(0)

    # Bestemmer karakter basert på scoren
    if score > 6:
        grade = 'A'
    elif score > 4:
        grade = 'B'
    elif score > 2:
        grade = 'C'
    elif score > 1:
        grade = 'D'
    else:
        grade = 'F'

    return grade  # Returnerer den beregnede karakteren

if __name__ == "__main__":
    url = input("Enter the GitHub contribution URL: ")  # Ber brukeren om å skrive inn GitHub URL
    grade = get_grade(url)  # Kaller get_grade-funksjonen for å beregne karakteren
    print(f"GitHub Grade: {grade}")  # Skriver ut den beregnede karakteren