python
import sympy as sp

# Define time variable and position vector as functions of time
t = sp.symbols('t')
x, y, z = sp.symbols('x y z', cls=sp.Function)

# Position vector
r = sp.Matrix([x(t), y(t), z(t)])

# Velocity as the first derivative of position with respect to time
v = r.diff(t)
print(f"Velocity v(t): {v}")

# Acceleration as the second derivative of position with respect to time
a = v.diff(t)
print(f"Acceleration a(t): {a}")