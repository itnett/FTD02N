python
from sympy import simplify, sin, cos, tan

uttrykk = sin(x)**2 + cos(x)**2
forenklet_uttrykk = simplify(uttrykk)
print(forenklet_uttrykk)  # Output: 1

uttrykk2 = sin(x)/cos(x)
forenklet_uttrykk2 = simplify(uttrykk2)
print(forenklet_uttrykk2)  # Output: tan(x)