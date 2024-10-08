python
from sympy import symbols, expand, factor
a, b = symbols('a b')
expr = a**2 - b**2
expanded_expr = expand(expr)
factored_expr = factor(expanded_expr)
print("Expanded expression:", expanded_expr)
print("Factored expression:", factored_expr)