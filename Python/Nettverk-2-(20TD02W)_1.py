python
import networkx as nx
import matplotlib.pyplot as plt

# Opprett en graf for nettverkstopologien
G = nx.Graph()
G.add_edges_from([('Ruter1', 'Switch1'), ('Switch1', 'PC1'), ('Switch1', 'PC2')])

# Tegn grafen
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500)
plt.title('Nettverkstopologi')
plt.show()

# Analyser nettverkstrafikk (eksempel)
import pandas as pd

data = pd.read_csv('nettverkstrafikk.csv')
plt.figure(figsize=(10, 6))
plt.plot(data['Tid'], data['Trafikkmengde'])
plt.title('Nettverkstrafikk over tid')
plt.xlabel('Tid')
plt.ylabel('Trafikkmengde')
plt.show()