python
from sympy import symbols, Eq, solve

# Definer symbolene for de ukjente
x, y = symbols('x y')

# Definer likningene
eq1 = Eq(2*x + 3*y, 7)
eq2 = Eq(x - y, 1)

# Løs likningssettet
solution = solve((eq1, eq2), (x, y))

# Skriv ut løsningen
print(solution)