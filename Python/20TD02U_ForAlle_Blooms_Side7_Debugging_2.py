python
   import logging

   logging.basicConfig(level=logging.INFO)

   def addisjon(a, b):
       logging.info(f"Legger sammen {a} og {b}")
       return a + b

   resultat = addisjon(5, 3)
   logging.info(f"Resultat: {resultat}")