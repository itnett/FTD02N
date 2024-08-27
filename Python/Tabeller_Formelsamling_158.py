python
from fractions import Fraction

# Brøkregning
a = Fraction(3, 4)  # Brøken 3/4
b = Fraction(1, 2)  # Brøken 1/2

print("a + b =", a + b)  # Output: 5/4
print("a - b =", a - b)  # Output: 1/4
print("a * b =", a * b)  # Output: 3/8
print("a / b =", a / b)  # Output: 3/2

# Prosentregning
prosent = 75  # 75%
desimaltall = prosent / 100

print(prosent, "% =", desimaltall)  # Output: 75 % = 0.75