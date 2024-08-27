python
from sympy import symbols, Eq, nonlinsolve

n, e, d = symbols('n e d')  # Modulus, offentlig nøkkel, privat nøkkel

# Ligninger for RSA-kryptering
ligning1 = Eq(e*d, 1) 
ligning2 = Eq((p-1)*(q-1), n)

løsning = nonlinsolve([ligning1, ligning2], (p, q))
print(løsning)