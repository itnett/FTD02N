python
import sympy as sp

# Vector algebra operations
v1 = sp.Matrix([1, 2, 3])
v2 = sp.Matrix([4, 5, 6])

dot_product = v1.dot(v2)
cross_product = v1.cross(v2)

print("v1 =", v1)
print("v2 =", v2)
print("Dot product:", dot_product)
print("Cross product:", cross_product)