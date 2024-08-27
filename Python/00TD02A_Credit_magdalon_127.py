python
from sympy import factor

n = 15
e = 7
phi = (p-1)*(q-1)  # Eulers totient-funksjon
d = mod_inverse(e, phi)

print(f"Privat nøkkel (d): {d}")