python
import sympy as sp

# Define symbols
x, y = sp.symbols('x y')
x1, y1, x2, y2 = sp.symbols('x1 y1 x2 y2')

# Equation of the line through points (x1, y1) and (x2, y2)
slope = (y2 - y1) / (x2 - x1)
line_eq = sp.Eq(y - y1, slope * (x - x1))

print(f"Equation of the line: {line_eq}")