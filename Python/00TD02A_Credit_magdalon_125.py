python
from sympy import Symbol, symbols, pi, exp, ln, log, sqrt, simplify, expand

x = Symbol('x')
y = Symbol('y')
a, b, c = symbols('a b c')

uttrykk = 2*x + 3*y
print(uttrykk)  # Output: 2*x + 3*y

forenklet_uttrykk = simplify((x**2 + 2*x + 1)/(x + 1))
print(forenklet_uttrykk)  # Output: x + 1