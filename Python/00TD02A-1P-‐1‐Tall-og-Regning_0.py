python
# Lesson 1.1: Mental Arithmetic

# Addition
def mental_addition(a, b):
    return a + b

# Subtraction
def mental_subtraction(a, b):
    return a - b

# Multiplication
def mental_multiplication(a, b):
    return a * b

# Division
def mental_division(a, b):
    return a / b

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Perform operations
print(f"Addition: {a} + {b} = {mental_addition(a, b)}")
print(f"Subtraction: {a} - {b} = {mental_subtraction(a, b)}")
print(f"Multiplication: {a} * {b} = {mental_multiplication(a, b)}")
print(f"Division: {a} / {b} = {mental_division(a, b)}")