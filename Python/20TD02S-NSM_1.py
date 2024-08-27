python
import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges
nodes = {
    'Sikkerhetsledelse': ['Styring og risikohåndtering', 'Ressurstildeling', 'Hendelseshåndtering', 'Kontinuerlig forbedring'],
    'Fysisk sikkerhet': ['Adgangskontroll', 'Overvåkning', 'Fysiske barrierer', 'Sikkerhetspersonell'],
    'Personsikkerhet': ['Bakgrunnssjekk', 'Sikkerhetsopplæring', 'Klare roller og ansvar', 'Overvåkning og etterlevelse'],
    'IKT-sikkerhet': ['Nettverkssikkerhet', 'Systemintegritet', 'Databeskyttelse', 'Bevissthet om cybersikkerhet']
}

for parent, children in nodes.items():
    for child in children:
        G.add_edge(parent, child)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=3000, font_size=10, font_weight="bold", arrows=True, arrowstyle="-|>", arrowsize=20)
plt.title("NSMs Grunnprinsipper", size=15)
plt.show()