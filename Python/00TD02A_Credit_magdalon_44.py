python
import networkx as nx
import matplotlib.pyplot as plt

# Opprett en graf som representerer nettverkstopologien
G = nx.Graph()
G.add_nodes_from(["Router", "Switch", "Server1", "Server2", "PC1", "PC2"])
G.add_edges_from([
    ("Router", "Switch"),
    ("Switch", "Server1"),
    ("Switch", "Server2"),
    ("Switch", "PC1"),
    ("Switch", "PC2"),
])

# Tegn grafen
pos = nx.spring_layout(G)  # Posisjoner nodene automatisk
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
plt.title("Nettverkstopologi")
plt.show()