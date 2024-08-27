python
import sympy as sp

# Define symbols
vx, vy, vz = sp.symbols('vx vy vz')
v = sp.Matrix([vx, vy, vz])

# Vector representation
vector_representation = sp.Matrix([vx, vy, vz])
print(f"Vector representation: v = {vector_representation[0]}i + {vector_representation[1]}j + {vector_representation[2]}k")

# Magnitude of the vector
magnitude = sp.sqrt(vx**2 + vy**2 + vz**2)
print(f"Vector magnitude: |v| = {magnitude}")