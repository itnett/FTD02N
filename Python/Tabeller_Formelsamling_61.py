python
import sympy as sp

# Define symbols
x, y = sp.symbols('x y')
m, n, p = sp.symbols('m n p')

# Equation of the parabola
parabola_eq = sp.Eq((y - n)**2, 2 * p * (x - m))
print(f"Equation of the parabola: {parabola_eq}")

# Vertex of the parabola
vertex = (m, n)
print(f"Vertex of the parabola: {vertex}")

# Focus of the parabola
focus = (m + p / 2, n)
print(f"Focus of the parabola: {focus}")

# Directrix of the parabola
directrix = sp.Eq(x, m - p / 2)
print(f"Directrix of the parabola: {directrix}")