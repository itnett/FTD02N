python
from sympy import Sum, symbols

n = symbols('n')
nedetid_per_feil = 30  # Minutter
sannsynlighet_for_feil = 0.01
gjennomsnittlig_tid_mellom_feil = 1000  # Minutter

forventet_nedetid = (
    Sum(nedetid_per_feil * sannsynlighet_for_feil**n, (n, 1, oo)) * gjennomsnittlig_tid_mellom_feil
).doit()
print(f"Forventet nedetid per måned: {forventet_nedetid:.2f} minutter")