python
# Regneregler for potenser
a = 2
b = 3
m = 4
n = 5

print(f"{a}^0 = {a**0}")              # Output: 2^0 = 1
print(f"{a}^-n = 1/{a}^{n} = {a**-n}") # Output: 2^-5 = 1/2^5 = 0.03125
print(f"{a}^m * {a}^n = {a}^(m+n) = {a**(m+n)}")  # Output: 2^4 * 2^5 = 2^(4+5) = 512
print(f"({a}^m)^n = {a}^(m*n) = {a**(m*n)}")    # Output: (2^4)^5 = 2^(4*5) = 1048576
print(f"({a} * {b})^n = {a}^n * {b}^n = {a**n * b**n}")  # Output: (2 * 3)^5 = 2^5 * 3^5 = 7776