python
# Define point C
c1, c2, c3 = sp.symbols('c1 c2 c3')

# Vectors AB and AC
AC = sp.Matrix([c1 - a1, c2 - a2, c3 - a3])

# Normal vector to the plane
N = AB.cross(AC)

# Plane equation
x, y, z = sp.symbols('x y z')
plane_eq = N[0]*(x - a1) + N[1]*(y - a2) + N[2]*(z - a3)
plane_eq_simplified = sp.simplify(plane_eq)

print(f"Plane equation: {plane_eq_simplified} = 0")