python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
for i in range(6):
    print(f"{i}! = {factorial(i)}")