python
# Lesson 1.3: Prime Numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# List prime numbers between 1 and 20
print("Prime numbers between 1 and 20:")
for num in range(1, 21):
    if is_prime(num):
        print(num, end=" ")

# Check if a number is prime
number = int(input("\nEnter a number to check if it's prime: "))
print(f"Is {number} a prime number? {'Yes' if is_prime(number) else 'No'}")