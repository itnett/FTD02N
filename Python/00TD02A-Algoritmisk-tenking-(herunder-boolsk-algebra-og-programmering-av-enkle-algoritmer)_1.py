python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import networkx as nx

G = nx.DiGraph()
steps = ['Start', 'Take two slices of bread', 'Spread butter on one slice', 'Add ham', 'Add cheese', 'Put the other slice on top', 'Sandwich is ready']
edges = [(steps[i], steps[i+1]) for i in range(len(steps)-1)]
G.add_edges_from(edges)

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
plt.title('Algorithm for Making a Sandwich')
plt.show()