python
import requests
from bs4 import BeautifulSoup

def ndla_search(query):
    base_url = "https://ndla.no/search"
    params = {
        "query": query,
        "filter": "all"  # Søk i alle typer innhold
    }
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    results = []
    for result_element in soup.find_all('article', class_='search-result'):
        title_element = result_element.find('h3', class_='search-result__title')
        if title_element:
            title = title_element.text.strip()
            url = title_element.find('a')['href']
            results.append((title, url))
    return results

search_terms = [
    "Norsk", "Studieteknikk", "God skriftlig og muntlig kommunikasjon", 
    "Struktur, leservennlig layout", "Mål- og mottakerbevissthet", 
    "Yrkesrelevante sjangre", "Argumentasjon og drøfting", 
    "Tverrfaglige prosjekter", "Prosjektarbeid", "Prosjektledelse", 
    "Samarbeidslæring", "Kritisk kildebruk", "Søking, bearbeiding og presentasjon av data", 
    "IKT-verktøy", "Konstruktive tilbakemeldinger", "Refleksjon over egen læring", 
    "Etiske refleksjoner", "Engelsk", "Grammatikk", "Setningsoppbygging", 
    "Fagterminologi", "Forståelse av tekster", "Produksjon av egne tekster", 
    "Tverrkulturell forståelse", "Diskusjoner", "Presentasjoner", "Gruppearbeid"
]

for term in search_terms:
    results = ndla_search(term)
    print(f"\n**{term}:**")
    if results:
        for title, url in results[:3]:  # Vis de 3 første resultatene
            print(f"- {title}: {url}")
    else:
        print("- Ingen resultater funnet")