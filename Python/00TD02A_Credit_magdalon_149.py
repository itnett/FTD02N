python
from sympy import solveset, S

ligning = sin(x) - 1/2
løsninger = solveset(ligning, x, domain=S.Reals)
print(løsninger)  # Output: [pi/6 + 2*pi*n, 5*pi/6 + 2*pi*n]