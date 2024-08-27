python
import sympy as sp

# Define symbols
x, y = sp.symbols('x y')
m, n, a, b = sp.symbols('m n a b')

# Equation of the hyperbola
hyperbola_eq = sp.Eq((x - m)**2 / a**2 - (y - n)**2 / b**2, 1)
print(f"Equation of the hyperbola: {hyperbola_eq}")

# Center of the hyperbola
center = (m, n)
print(f"Center of the hyperbola: {center}")

# Semi-major and semi-minor axes
semi_real_axis = a
semi_imaginary_axis = b
print(f"Semi-real axis (a): {semi_real_axis}")
print(f"Semi-imaginary axis (b): {semi_imaginary_axis}")

# Calculate the focal length
c = sp.sqrt(a**2 + b**2)
print(f"Focal length (c): {c}")

# Calculate the eccentricity
e = c / a
print(f"Eccentricity (e): {e}")

# Calculate the semi-latus rectum (p)
p = b**2 / a
print(f"Semi-latus rectum (p): {p}")

# Asymptotes of the hyperbola
asymptote1 = sp.Eq((x - m) / a - (y - n) / b, 0)
asymptote2 = sp.Eq((x - m) / a + (y - n) / b, 0)
print(f"Asymptote 1: {asymptote1}")
print(f"Asymptote 2: {asymptote2}")