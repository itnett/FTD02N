python
import matplotlib.pyplot as plt
import numpy as np

# Antenna positions
antenna1 = (0, 0)
antenna2 = (5, 3)

# Calculate distance
distance = np.sqrt((antenna2[0] - antenna1[0])**2 + (antenna2[1] - antenna1[1])**2)

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(*zip(antenna1, antenna2), marker='x', s=100, color='red')
plt.plot([antenna1[0], antenna2[0]], [antenna1[1], antenna2[1]], linestyle='--')
plt.text((antenna1[0] + antenna2[0])/2, (antenna1[1] + antenna2[1])/2 + 0.5, f'Distance: {distance:.2f}', ha='center')
plt.title('Antenna Placement')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()