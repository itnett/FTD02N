python
# Lesson 1.7: Order of Operations

def order_of_operations(expression):
    return eval(expression)

# Input
expression = input("Enter a mathematical expression: ")

# Calculate result
print(f"Result: {expression} = {order_of_operations(expression)}")