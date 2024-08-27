python
from sympy import symbols, Eq, nonlinsolve

x, y = symbols('x y')
ligning1 = Eq(x**2 + y**2, 25)  # Ligning for en sirkel med radius 5
ligning2 = Eq(y, x + 1)         # Ligning for en rett linje

løsning = nonlinsolve([ligning1, ligning2], (x, y))
print(løsning)  # Output: {(-4, -3), (3, 4)}