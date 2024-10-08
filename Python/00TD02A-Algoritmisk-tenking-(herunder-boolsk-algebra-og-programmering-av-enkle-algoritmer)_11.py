python
import matplotlib.pyplot as plt

# Data
iterations = list(range(1, 11))
values = [i*2 for i in iterations]

# Plot
plt.plot(iterations, values, marker='o')
plt.title('For Loop Example: Doubling Values')
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.grid(True)
plt.show()