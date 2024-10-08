python
import matplotlib.pyplot as plt
import numpy as np

# Generate data
np.random.seed(42)  # for reproducibility
load = np.random.uniform(0, 200, 1000)
response_time = np.random.uniform(0, 10, 1000)

# Classify server states
server_states = np.array(["Normal" if l < 100 and r < 2 else 
                         "Overloaded" if 100 <= l < 180 and r < 5 else
                         "Crash" for l, r in zip(load, response_time)])

# Create the plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(load, response_time, c=server_states, cmap="viridis", alpha=0.7)
plt.title("Web Server Phase Diagram")
plt.xlabel("Load")
plt.ylabel("Response Time (s)")

# Add legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=state, markerfacecolor=scatter.cmap(scatter.norm(state)), markersize=8) for state in np.unique(server_states)]
plt.legend(handles=legend_elements, title="Server State")

plt.grid(True)
plt.show()