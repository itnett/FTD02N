python
from sympy import Function, dsolve, Eq, symbols

t = symbols('t')
y = Function('y')
diffeq = Eq(y(t).diff(t, t) - y(t), exp(t))  # Differensialligningen y'' - y = e^t

løsning = dsolve(diffeq, y(t))
print(løsning)