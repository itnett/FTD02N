python
import sympy as sp

# Define symbols
t = sp.symbols('t')
a1, a2, a3 = sp.symbols('a1 a2 a3')
b1, b2, b3 = sp.symbols('b1 b2 b3')

# Parametric equations of the line through points A and B
x = a1 + t * (b1 - a1)
y = a2 + t * (b2 - a2)
z = a3 + t * (b3 - a3)

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")