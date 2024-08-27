python
from sympy import div, Symbol

x = Symbol('x')
teller = x**3 + 2*x**2 - x - 2
nevner = x - 1

kvotient, rest = div(teller, nevner)
print(f"Kvotient: {kvotient}, Rest: {rest}")  # Output: Kvotient: x**2 + 3*x + 2, Rest: 0