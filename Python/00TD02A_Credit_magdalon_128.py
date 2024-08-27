python
from sympy import Symbol, Eq, solveset

x = Symbol('x')
ligning = Eq(2*x + 3, 5)
løsning = solveset(ligning, x)
print(løsning)  # Output: {1}