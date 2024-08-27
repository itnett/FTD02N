python
   try:
       # Forsøk å legge til en transaksjon med negativ verdi
       t = Transaksjon('2024-09-01', 'Bankkonto', -10000, 'Debet')
   except ValueError as e:
       print(f"Feil: {e}")