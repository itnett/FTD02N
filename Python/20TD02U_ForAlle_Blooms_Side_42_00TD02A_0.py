python
# Løs likningen 2x + 3 = 7
from sympy import symbols, Eq, solve

x = symbols('x')
likning = Eq(2*x + 3, 7)
løsning = solve(likning, x)
print(løsning)  # Output: [2]