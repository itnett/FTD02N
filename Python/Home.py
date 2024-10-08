python
# List example
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Binary Tree example
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal of binary tree:", end=' ')
inorder_traversal(root)