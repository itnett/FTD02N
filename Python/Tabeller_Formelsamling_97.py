python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate the factorial of 5
print(f"Factorial of 5: {factorial(5)}")