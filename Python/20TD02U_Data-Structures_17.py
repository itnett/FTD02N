python
def reverse_string(input_string):
    stack = []
    
    # Push all characters of the string onto the stack
    for char in input_string:
        stack.append(char)
    
    reversed_string = ""
    
    # Pop all characters from the stack to get them in reverse order
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
input_string = "hello"
print(reverse_string(input_string))  # Output: "olleh"