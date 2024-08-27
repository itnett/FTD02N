python
from sympy import Symbol, symbols, lambdify, diff

x = Symbol('x')
f = x**3 / 3 - x**2 - x / 3 + 1
print(f)  # Output: x**3/3 - x**2 - x/3 + 1