python
# Lesson 1.8: Parentheses

def calculate_with_parentheses(expression):
    return eval(expression)

# Input
expression = input("Enter a mathematical expression with parentheses: ")

# Calculate result
print(f"Result: {expression} = {calculate_with_parentheses(expression)}")