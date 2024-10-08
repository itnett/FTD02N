python
class MinStack:
    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, x):
        self.mainStack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        if self.mainStack:
            top = self.mainStack.pop()
            if top == self.minStack[-1]:
                self.minStack.pop()

    def top(self):
        if self.mainStack:
            return self.mainStack[-1]

    def getMin(self):
        if self.minStack:
            return self.minStack[-1]