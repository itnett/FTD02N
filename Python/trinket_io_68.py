python
   # Beregne kombinasjoner
   n = 10
   r = 3
   combinations = factorial(n) / (factorial(r) * factorial(n - r))
   print(f"Kombinasjoner av 10 objekter tatt 3 om gangen: {combinations}")