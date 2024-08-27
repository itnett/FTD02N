python
from sympy import factorial

# Permutations (nPk)
def permutations(n, k):
    return factorial(n) / factorial(n - k)

# Combinations (nCk)
def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

n, k = 5, 3
print(f"Permutations P({n}, {k}): {permutations(n, k)}")
print(f"Combinations C({n}, {k}): {combinations(n, k)}")