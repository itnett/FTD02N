python
# Define vectors a and b
ax, ay, az = sp.symbols('ax ay az')
bx, by, bz = sp.symbols('bx by bz')

# Dot product
dot_product = ax*bx + ay*by + az*bz
print(f"Dot product: a · b = {dot_product}")

# Magnitude-based dot product
magnitude_a = sp.sqrt(ax**2 + ay**2 + az**2)
magnitude_b = sp.sqrt(bx**2 + by**2 + bz**2)
angle_phi = sp.symbols('phi')
dot_product_magnitude = magnitude_a * magnitude_b * sp.cos(angle_phi)
print(f"Dot product (magnitude-based): a · b = {dot_product_magnitude}")