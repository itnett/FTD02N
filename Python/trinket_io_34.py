python
from sympy import diff

x = symbols('x')
poly_function = x**3 - 6*x**2 + 11*x - 6
poly_diff = diff(poly_function, x)
print(f"Derivative of the polynomial function: {poly_diff}")