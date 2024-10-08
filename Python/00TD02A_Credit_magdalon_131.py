python
from sympy import symbols, Eq, linsolve

x, y = symbols('x y')
ligning1 = Eq(2*x + 3*y, 8)
ligning2 = Eq(x - 2*y, -3)

løsning = linsolve([ligning1, ligning2], (x, y))
print(løsning)  # Output: {(1, 2)}