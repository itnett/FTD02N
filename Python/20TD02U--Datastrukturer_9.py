python
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

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, vals):
        if node:
            vals = self._inorder_traversal(node.left, vals)
            vals.append(node.val)
            vals = self._inorder_traversal(node.right, vals)
        return vals

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, node, vals):
        if node:
            vals.append(node.val)
            vals = self._preorder_traversal(node.left, vals)
            vals = self._preorder_traversal(node.right, vals)
        return vals

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, node, vals):
        if node:
            vals = self._postorder_traversal(node.left, vals)
            vals = self._postorder_traversal(node.right, vals)
            vals.append(node.val)
        return vals

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

# AVL Tree Implementation
class AVLTreeNode(TreeNode):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1

class AVLTree(BinaryTree):
    def insert(self, key):
        if not self.root:
            self.root = AVLTreeNode(key)
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLTreeNode(key)
        if key < node.val:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and key < node.left.val:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.val:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.val:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.val:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 

1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)