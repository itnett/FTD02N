python
import networkx as nx

# Create the graph
G = nx.DiGraph()
G.add_edges_from([("Blocking", "Allowing"), ("Allowing", "Logging"), ("Logging", "Blocking")])

# Define positions for nodes (adjust as needed)
pos = {"Blocking": (0, 1), "Allowing": (1, 1), "Logging": (0.5, 0)}

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, arrows=True, node_size=2000, node_color="skyblue", font_size=12)
plt.title("Firewall State Diagram")
plt.show()