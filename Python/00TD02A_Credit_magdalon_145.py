python
from sympy import sin, cos, tan, pi, symbols

x = symbols('x')
uttrykk = sin(x)**2 + cos(x)**2
print(uttrykk.simplify())  # Output: 1