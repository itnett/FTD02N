python
from sympy import apart, together, cancel

uttrykk = (x**2 + 2*x + 1)/(x + 1)

delbrøksoppspalting = apart(uttrykk)
print(delbrøksoppspalting)  # Output: x + 1

fellesnevner = together(delbrøksoppspalting)
print(fellesnevner)  # Output: (x**2 + 2*x + 1)/(x + 1)

forkortet_uttrykk = cancel(fellesnevner)
print(forkortet_uttrykk)  # Output: x + 1