python
from sympy import Sum, symbols, oo

n = symbols('n')
a0 = 1  # Første ledd
d = 2  # Differanse mellom leddene

rekke = Sum(a0 + d*n, (n, 0, oo))
print(rekke)  # Output: Sum(2*n + 1, (n, 0, oo))