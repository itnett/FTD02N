python
# Cross product
cross_product = sp.Matrix([
    ay*bz - az*by,
    az*bx - ax*bz,
    ax*by - ay*bx
])
print(f"Cross product: a × b = {cross_product[0]}i + {cross_product[1]}j + {cross_product[2]}k")

# Magnitude of the cross product
cross_product_magnitude = magnitude_a * magnitude_b * sp.sin(angle_phi)
print(f"Cross product magnitude: |a × b| = {cross_product_magnitude}")