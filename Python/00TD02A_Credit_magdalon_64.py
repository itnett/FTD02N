python
import numpy as np

a = 5
b = 7
c = 8

# Cosinussetningen
cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
A = np.arccos(cos_A)
A_grader = np.degrees(A)

print(f"Vinkel A: {A_grader:.2f} grader")