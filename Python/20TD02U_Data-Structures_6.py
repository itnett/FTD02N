python
def reverse_string(text):
  """
  Reverses a string using a stack.
  """
  stack = []  # Create an empty stack
  for char in text:
    stack.append(char)  # Push each character onto the stack

  reversed_text = ""
  while stack:  # While the stack is not empty
    reversed_text += stack.pop()  # Pop characters and add to the reversed string

  return reversed_text

# Example usage
original_text = "Hello, world!"
reversed_text = reverse_string(original_text)
print(f"Original: {original_text}")
print(f"Reversed: {reversed_text}")