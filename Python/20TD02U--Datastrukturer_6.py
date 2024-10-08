python
class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            if item == self.min_stack[-1]:
                self.min_stack.pop()
            return item
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def get_min(self):
        if not self.is_empty():
            return self.min_stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack