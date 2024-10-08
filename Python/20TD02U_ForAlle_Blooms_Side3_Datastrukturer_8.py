python
class Deque:
    def __init__(self):
        self.deque = []

    def append_front(self, item):
        self.deque.insert(0, item)

    def append_back(self, item):
        self.deque.append(item)

    def pop_front(self):
        return self.deque.pop(0)

    def pop_back(self):
        return self.deque.pop()

# Bruk av Deque
dq = Deque()
dq.append_front(1)
dq.append_back(2)
print(dq.pop_front())  # Utdata: 1
print(dq.pop_back())   # Utdata: 2