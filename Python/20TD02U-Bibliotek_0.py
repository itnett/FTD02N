python
import requests

def hent_bokinformasjon(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()
    if data["totalItems"] > 0:
        bok = data["items"][0]["volumeInfo"]
        return f"Tittel: {bok['title']}, Forfatter: {bok['authors']}"
    else:
        return "Fant ikke boken"

print(hent_bokinformasjon("9788205511112"))