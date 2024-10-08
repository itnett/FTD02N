python
import matplotlib.pyplot as plt
import numpy as np

# Define mass (constant)
mass = 1.0  # kg

# Create an array of velocities
velocities = np.linspace(0, 10, 100)  # m/s

# Calculate kinetic energy for each velocity
kinetic_energy = 0.5 * mass * velocities**2

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(velocities, kinetic_energy, marker='o', linestyle='-', color='blue')
plt.title('Kinetic Energy vs. Velocity')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Kinetic Energy (J)')
plt.grid(True)
plt.show()