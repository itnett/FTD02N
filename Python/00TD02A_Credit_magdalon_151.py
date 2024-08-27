python
from sympy import div, Symbol

n = Symbol('n')
tid_kompleksitet = 2*n**3 + 5*n**2 + 10*n + 15

# Del på n for å finne den dominerende termen
kvotient, _ = div(tid_kompleksitet, n)
print(f"Dominerende term: {kvotient}")  # Output: Dominerende term: 2*n**2 + 5*n + 10