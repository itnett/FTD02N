python
print("\nAlgorithmic Thinking")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(f"GCD of 48 and 18: {gcd(48, 18)}")