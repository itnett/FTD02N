python
import sympy as sp

# Define symbols
x = sp.symbols('x')
y = sp.Function('y')(x)

# First and second derivatives of y with respect to x
y_prime = sp.diff(y, x)
y_double_prime = sp.diff(y_prime, x)

# Radius of curvature formula
R = ((1 + y_prime**2)**(3/2)) / sp.Abs(y_double_prime)
print(f"Radius of curvature (explicit): {R}")