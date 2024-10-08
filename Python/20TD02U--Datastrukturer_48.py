python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node:
            result = self._inorder_traversal(node.left, result)
            result.append(node.value)
            result = self._inorder_traversal(node.right, result)
        return result

# Bruk av BinaryTree
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
print(bt.inorder_traversal())  # Output: [5, 10, 15]