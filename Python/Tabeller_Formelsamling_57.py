python
# Define symbols
A, B, C = sp.symbols('A B C')

# Point (x1, y1)
x1, y1 = sp.symbols('x1 y1')

# Distance from point to line Ax + By + C = 0
distance = sp.Abs(A * x1 + B * y1 + C) / sp.sqrt(A**2 + B**2)

print(f"Distance from point to line: {distance}")