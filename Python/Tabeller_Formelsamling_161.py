python
from sympy import Symbol, factor, expand

# Sammentrekning
x = Symbol('x')
uttrykk = 2*x + 3*x - 5

sammentrukket = uttrykk.simplify()
print("Sammentrukket uttrykk:", sammentrukket)  # Output: 5*x - 5

# Faktorisering
uttrykk2 = x**2 + 5*x + 6

faktorisert = factor(uttrykk2)
print("Faktorisert uttrykk:", faktorisert)  # Output: (x + 2)*(x + 3)

# Utvide (motsatt av faktorisering)
utvidet = expand(faktorisert)
print("Utvidet uttrykk:", utvidet)  # Output: x**2 + 5*x + 6