python
from sympy import integrate

g = 2*x + 1
integral_g = integrate(g, x)

print("g(x) =", g)
print("∫g(x) dx =", integral_g)