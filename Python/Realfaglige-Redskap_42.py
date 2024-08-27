python
from collections import deque

# Kø
queue = deque()
queue.append("første")
queue.append("andre")
print(queue.popleft())  # Output: "første"

# Stakk
stack = []
stack.append("første")
stack.append("andre")
print(stack.pop())  # Output: "andre"