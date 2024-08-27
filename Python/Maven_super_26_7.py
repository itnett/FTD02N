python
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Opprette noder
root = Node("root")
child1 = Node("child1")
child2 = Node("child2")

# Bygge treet
root.add_child(child1)
root.add_child(child2)

print(root.data)  # Utskrift: root