python
# Define vector c
cx, cy, cz = sp.symbols('cx cy cz')

# Scalar triple product
scalar_triple_product = cross_product.dot(sp.Matrix([cx, cy, cz]))
print(f"Scalar triple product: (a × b) · c = {scalar_triple_product}")

# Vector triple product
vector_triple_product = (cross_product.cross(sp.Matrix([cx, cy, cz])))
print(f"Vector triple product: a × (b × c) = {vector_triple_product}")

# Lagrange's identity
d1x, d1y, d1z = sp.symbols('d1x d1y d1z')
d2x, d2y, d2z = sp.symbols('d2x d2y d2z')
a_cross_b = sp.Matrix([ax, ay, az]).cross(sp.Matrix([bx, by, bz]))
c_cross_d = sp.Matrix([cx, cy, cz]).cross(sp.Matrix([d1x, d1y, d1z]))
lagrange_identity = a_cross_b.dot(c_cross_d)
print(f"Lagrange's identity: (a × b) · (c × d) = {lagrange_identity}")