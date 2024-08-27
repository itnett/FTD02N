python
import cmath

def solve_quadratic(a, b, c):
    """Løs en andregradslikning på formen ax^2 + bx + c = 0."""
    d = b**2 - 4*a*c  # diskriminanten
    if d >= 0:
        root1 = (-b + cmath.sqrt(d)) / (2*a)
        root2 = (-b - cmath.sqrt(d)) / (2*a)
    else:
        root1 = (-b + cmath.sqrt(d)) / (2*a)
        root2 = (-b - cmath.sqrt(d)) / (2*a)
    return root1, root2