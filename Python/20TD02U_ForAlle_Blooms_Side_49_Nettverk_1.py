python
import networkx as nx
import matplotlib.pyplot as plt

# Simulerer en stjernetopologi
star_topology = nx.Graph()
star_topology.add_edges_from([("Switch", "PC1"), ("Switch", "PC2"), ("Switch", "PC3")])

nx.draw(star_topology, with_labels=True, node_size=3000, node_color='skyblue')
plt.show()