python
import sympy as sp

# Define the symbols
A, B, C, a, b, c, s = sp.symbols('A B C a b c s')

# Sum of angles in a triangle
sum_of_angles = sp.Eq(A + B + C, 180)
print(f"Sum of angles in a triangle: {sum_of_angles}")

# Law of sines
law_of_sines = sp.Eq(sp.sin(A)/a, sp.sin(B)/b)
print(f"Law of sines: {law_of_sines}")

# Law of cosines
law_of_cosines = sp.Eq(a**2, b**2 + c**2 - 2*b*c*sp.cos(A))
print(f"Law of cosines: {law_of_cosines}")

# Area of a triangle (using sine)
area_sine = sp.Rational(1, 2) * b * c * sp.sin(A)
print(f"Area of triangle (using sine): {area_sine}")

# Semi-perimeter
semi_perimeter = sp.Rational(1, 2) * (a + b + c)
print(f"Semi-perimeter (s): {semi_perimeter}")

# Heron's formula
F = sp.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
print(f"Heron's formula: {F}")

# Tangent of half-angle
tan_A_half = sp.tan(A/2)
tan_A_half_formula = sp.Eq(tan_A_half, F / (semi_perimeter * (semi_perimeter - a)))
print(f"Tangent of half-angle (A/2): {tan_A_half_formula}")