python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def display(self):
        levels = []
        self._display(self.root, 0, levels)
        return levels

    def _display(self, node, level, levels):
        if node:
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            self._display(node.left, level + 1, levels)
            self._display(node.right, level + 1, levels)