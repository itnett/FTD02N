python
   from math import factorial

   # Beregne sannsynligheten for å få en bestemt kombinasjon
   n = 5
   r = 3
   combinations = factorial(n) / (factorial(r) * factorial(n - r))
   print(f"Kombinasjoner av 5 tatt 3 om gangen: {combinations}")