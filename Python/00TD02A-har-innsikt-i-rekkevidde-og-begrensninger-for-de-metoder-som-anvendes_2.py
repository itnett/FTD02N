python
import matplotlib.pyplot as plt

# Data sizes in bytes
sizes = {'Kilobyte (KB)': 1e3, 'Megabyte (MB)': 1e6, 'Gigabyte (GB)': 1e9, 'Terabyte (TB)': 1e12}

# Plot
plt.figure(figsize=(10, 6))
plt.bar(sizes.keys(), sizes.values(), log=True)  # Use logarithmic scale for y-axis
plt.title('Data Size Comparison')
plt.ylabel('Size (Bytes)')
plt.show()