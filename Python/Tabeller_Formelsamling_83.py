python
# Boolean algebra
a, b = True, False
and_result = a and b
or_result = a or b
not_result = not a

print(f"Boolean AND: {a} and {b} = {and_result}")
print(f"Boolean OR: {a} or {b} = {or_result}")
print(f"Boolean NOT: not {a} = {not_result}")

# Simple algorithm (factorial using recursion)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"Factorial of 5: {factorial(5)}")