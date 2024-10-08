python
# List
my_list = [1, 2, 3, 4, 5]

# Stack
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())

# Queue
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
print(queue.popleft())

# Binary Tree
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value