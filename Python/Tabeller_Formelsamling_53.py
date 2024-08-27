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

# Define scalar field varphi as a function of x, y, z
varphi = sp.Function('varphi')(x, y, z)

# Gradient of the scalar field
grad_varphi = sp.Matrix([sp.diff(varphi, x), sp.diff(varphi, y), sp.diff(varphi, z)])
print(f"Gradient of varphi: grad_varphi = {grad_varphi}")