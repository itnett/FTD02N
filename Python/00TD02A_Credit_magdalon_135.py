python
from sympy import Symbol, solveset, S

x = Symbol('x')
ulikhet = x**2 - 4 < 0
løsning = solveset(ulikhet, x, domain=S.Reals)
print(løsning)  # Output: (-2, 2)