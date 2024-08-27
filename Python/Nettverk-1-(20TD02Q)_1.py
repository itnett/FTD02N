python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.star_graph(4)  # Oppretter en stjernetopologi med 5 noder (1 sentral, 4 ytre)
pos = nx.spring_layout(G)  # Posisjonerer nodene for visualisering

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=10)
plt.title("Enkel stjernetopologi")
plt.show()  # Viser grafen