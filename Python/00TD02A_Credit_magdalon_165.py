python
from sympy import Sum, symbols, oo

n = symbols('n')
a0 = 1  # Første ledd
r = 0.5  # Forhold mellom leddene

rekke = Sum(a0 * r**n, (n, 0, oo))
print(rekke)  # Output: Sum(0.5**n, (n, 0, oo))

if abs(r) < 1:
    summen = rekke.doit()
    print(f"Summen av rekken: {summen}")  # Output: Summen av rekken: 2
else:
    print("Rekken divergerer.")