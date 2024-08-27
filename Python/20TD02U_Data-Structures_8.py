python
def reverse_string(input_string):
    # Create an empty stack
    stack = []

    # Push all characters of the string onto the stack
    for char in input_string:
        stack.append(char)

    # Pop all characters from the stack and append them to the reversed_string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Test the function
input_string = "Hello, World!"
print(f"Original String: {input_string}")
print(f"Reversed String: {reverse_string(input_string)}")