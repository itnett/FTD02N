python
# Define scalar field varphi as a function of x, y, z
varphi = sp.Function('varphi')(x, y, z)

# Gradient of the scalar field
grad_varphi = sp.Matrix([sp.diff(varphi, x), sp.diff(varphi, y), sp.diff(varphi, z)])
print(f"Gradient of varphi: grad_varphi = {grad_varphi}")