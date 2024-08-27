python
from sympy import trigsimp

uttrykk = sin(x) + cos(x)
forenklet_uttrykk = trigsimp(uttrykk)
print(forenklet_uttrykk)  # Output: sqrt(2)*sin(x + pi/4)