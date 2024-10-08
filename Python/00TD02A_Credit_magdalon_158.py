python
from sympy import integrate, Symbol

x = Symbol('x')
ubestemt_integral = integrate(x**2, x)
print(ubestemt_integral)  # Output: x**3/3

bestemt_integral = integrate(x**2, (x, 0, 1))
print(bestemt_integral)  # Output: 1/3