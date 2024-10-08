python
# Lesson 1.4: Factoring

# Prime factorization
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

# Greatest Common Divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input
number = int(input("Enter a number for prime factorization: "))
print(f"Prime factors of {number}: {prime_factors(number)}")

# GCD calculation
a = int(input("Enter first number for GCD: "))
b = int(input("Enter second number for GCD: "))
print(f"GCD of {a} and {b} is: {gcd(a, b)}")