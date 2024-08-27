python
import sympy as sp

# Define symbols
x, y = sp.symbols('x y')
m, n, a, b = sp.symbols('m n a b')

# Equation of the ellipse
ellipse_eq = sp.Eq((x - m)**2 / a**2 + (y - n)**2 / b**2, 1)
print(f"Equation of the ellipse: {ellipse_eq}")

# Center of the ellipse
center = (m, n)
print(f"Center of the ellipse: {center}")

# Semi-major and semi-minor axes
semi_major_axis = a
semi_minor_axis = b
print(f"Semi-major axis (a): {semi_major_axis}")
print(f"Semi-minor axis (b): {semi_minor_axis}")

# Calculate the focal length
c = sp.sqrt(a**2 - b**2)
print(f"Focal length (c): {c}")

# Calculate the eccentricity
e = c / a
print(f"Eccentricity (e): {e}")

# Calculate the semi-latus rectum (p)
p = b**2 / a
print(f"Semi-latus rectum (p): {p}")