python
import json

def lagre_innstillinger(innstillinger, filnavn="innstillinger.json"):
    with open(filnavn, "w") as f:
        json.dump(innstillinger, f, indent=4)  # Formaterer JSON-dataene for bedre lesbarhet

def last_innstillinger(filnavn="innstillinger.json"):
    try:
        with open(filnavn, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Returner en tom ordbok hvis filen ikke finnes

# Brukerinnstillinger
innstillinger = {
    "tema": "mørkt",
    "font_størrelse": 12,
    "automatisk_lagring": True,
}

lagre_innstillinger(innstillinger)

# Laste inn innstillinger senere
lastede_innstillinger = last_innstillinger()
print(lastede_innstillinger)