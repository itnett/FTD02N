python
from difflib import SequenceMatcher

def sammenligne_tekster(tekst1, tekst2):
    return SequenceMatcher(None, tekst1, tekst2).ratio()

tekst1 = "Dette er en original tekst om teknologi."
tekst2 = "Dette er en kopi tekst om teknologi."
likhet = sammenligne_tekster(tekst1, tekst2)

print(f"Likheten mellom tekstene er: {likhet:.2f}")