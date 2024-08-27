python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

# Bruk av Stack
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Output: 3
print(s.peek())  # Output: 2