python
from sympy import Piecewise, Symbol

x = Symbol('x')
f = Piecewise((x**2, x < 0), (x, x >= 0))  # f(x) = x^2 hvis x < 0, ellers f(x) = x
print(f)  # Output: Piecewise((x**2, x < 0), (x, True))