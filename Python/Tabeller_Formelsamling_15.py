python
from sympy import Sum, oo

# Aritmetisk rekke
n = symbols('n')
aritmetisk_rekke = Sum(2*n + 1, (n, 1, oo))
print(aritmetisk_rekke)

# Geometrisk rekke
geometrisk_rekke = Sum(1/2**n, (n, 0, oo))
print(geometrisk_rekke)