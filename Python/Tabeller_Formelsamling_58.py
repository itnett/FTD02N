python
import sympy as sp

# Define symbols
x, y = sp.symbols('x y')
x1, y1, x2, y2 = sp.symbols('x1 y1 x2 y2')
k1, k2 = sp.symbols('k1 k2')
A, B, C = sp.symbols('A B C')

# Equation of the line through points (x1, y1) and (x2, y2)
slope = (y2 - y1) / (x2 - x1)
line_eq = sp.Eq(y - y1, slope * (x - x1))
print(f"Equation of the line: {line_eq}")

# Angle between two lines
angle = sp.atan((k2 - k1) / (1 + k1 * k2))
print(f"Angle between the lines: {angle} radians")

# Check for perpendicular lines
perpendicular_condition = sp.Eq(k1 * k2, -1)
print(f"Lines are perpendicular if: {perpendicular_condition}")

# Distance from point to line Ax + By + C = 0
distance = sp.Abs(A * x1 + B * y1 + C) / sp.sqrt(A**2 + B**2)
print(f"Distance from point to line: {distance}")