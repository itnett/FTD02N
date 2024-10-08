python
from sympy import symbols, Eq, solveset

P, L, C = symbols('P L C')  # Sannsynlighet for brudd, tap ved brudd, kostnad for mottiltak

# Ligning for forventet tap
forventet_tap = P * L

# Ligning for kostnadseffektivitet av mottiltak
kostnadseffektivitet = (P * L - (1 - P) * C) / C

# Løs for sannsynlighet for brudd gitt et akseptabelt tapnivå
løsning = solveset(forventet_tap - 10000, P)  # Akseptabelt tap på 10 000
print(løsning)