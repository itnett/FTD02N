python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ... (assume head and new_node are defined)
new_node.next = head.next 
head.next = new_node