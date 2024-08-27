python
# Define point P and vector AB
p1, p2, p3 = sp.symbols('p1 p2 p3')
AB = sp.Matrix([b1 - a1, b2 - a2, b3 - a3])
AP = sp.Matrix([p1 - a1, p2 - a2, p3 - a3])

# Cross product and distance calculation
cross_product = AB.cross(AP)
distance = cross_product.norm() / AB.norm()

print(f"Distance from point P to the line: {distance}")