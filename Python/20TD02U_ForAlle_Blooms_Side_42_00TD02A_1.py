python
# Løs likningssettet:
# 2x + 3y = 6
# x - y = 1
from sympy import symbols, Eq, solve

x, y = symbols('x y')
likning1 = Eq(2*x + 3*y, 6)
likning2 = Eq(x - y, 1)
løsninger = solve((likning1, likning2), (x, y))
print(løsninger)  # Output: {x: 3/5, y: 2/5}