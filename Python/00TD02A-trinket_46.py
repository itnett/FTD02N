python
print("\nCombinatorics")
from math import factorial
n = 5
r = 3
combinations = factorial(n) / (factorial(r) * factorial(n - r))
print(f"Combinations of 5 taken 3 at a time: {combinations}")