python
class Node:
    def __init__(self, name):
        self.name = name
        self.data_received = []

    def send_data(self, data, target_node):
        target_node.data_received.append(data)

# Simulerer LAN og WAN kommunikasjon
lan_node1 = Node("LAN_Node1")
lan_node2 = Node("LAN_Node2")
wan_node1 = Node("WAN_Node1")
wan_node2 = Node("WAN_Node2")

lan_node1.send_data("LAN Data", lan_node2)
wan_node1.send_data("WAN Data", wan_node2)

print(f"LAN_Node2 mottatt: {lan_node2.data_received}")
print(f"WAN_Node2 mottatt: {wan_node2.data_received}")