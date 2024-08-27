python
class Array:
    def __init__(self):
        self.array = []

    def insert(self, item):
        self.array.append(item)

    def remove(self, item):
        self.array.remove(item)

    def search(self, item):
        for i, value in enumerate(self.array):
            if value == item:
                return i
        return -1

    def display(self):
        return self.array