python
import sympy as sp

x, y = sp.symbols('x y')
uttrykk = 2*x**2 + 3*x - 5  # Eksempel på et algebraisk uttrykk

# Faktorisering
faktorisert = sp.factor(uttrykk)
print("Faktorisert uttrykk:", faktorisert)

# Løse likning
løsning = sp.solve(uttrykk, x)
print("Løsning av likningen:", løsning)