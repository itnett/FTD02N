python
import json

def les_konfigurasjon(filnavn):
    try:
        with open(filnavn, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Fant ikke konfigurasjonsfilen: {filnavn}")
        return {}  # Returner en tom ordbok hvis filen ikke finnes
    except json.JSONDecodeError:
        print(f"Ugyldig JSON-format i konfigurasjonsfilen: {filnavn}")
        return {}

konfigurasjon = les_konfigurasjon("config.json")
print(konfigurasjon)