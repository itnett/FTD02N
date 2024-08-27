python
     # Legge til logging i en funksjon
     import logging

     logging.basicConfig(level=logging.DEBUG)

     def add(a, b):
       logging.debug(f"Adding {a} and {b}")
       return a + b