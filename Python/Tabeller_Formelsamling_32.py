python
import sympy as sp

# Define points and vectors
P = sp.Point3D(1, 2, 3)
Q = sp.Point3D(4, 5, 6)
R = sp.Point3D(7, 8, 9)
line = sp.Line3D(P, Q)
plane = sp.Plane(P, Q, R)

print("Line equation:", line.equation())
print("Plane equation:", plane.equation())