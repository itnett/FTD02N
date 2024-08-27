python
import sympy as sp

x, y, z = sp.symbols('x y z')
f = sp.Function('f')(x, y, z)

# Gradient, divergence, and curl
grad_f = sp.Matrix([sp.diff(f, var) for var in (x, y, z)])
div_f = sp.diff(f, x) + sp.diff(f, y) + sp.diff(f, z)
curl_f = sp.Matrix([sp.diff(f, y) - sp.diff(f, z), sp.diff(f, z) - sp.diff(f, x), sp.diff(f, x) - sp.diff(f, y)])

print("Gradient of f:", grad_f)
print("Divergence of f:", div_f)
print("Curl of f:", curl_f)