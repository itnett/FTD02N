python
from sympy import symbols, And, solveset, S

x, y = symbols('x y')
ulikhet1 = x + y < 10
ulikhet2 = x - y > 2

løsning = solveset(And(ulikhet1, ulikhet2), (x, y), domain=S.Reals)
print(løsning)