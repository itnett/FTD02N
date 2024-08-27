python
# Define mass and gravitational acceleration (constants)
mass = 1.0  # kg
g = 9.81  # m/s^2

# Create an array of heights
heights = np.linspace(0, 10, 100)  # m

# Calculate potential energy for each height
potential_energy = mass * g * heights

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(heights, potential_energy, marker='o', linestyle='-', color='green')
plt.title('Potential Energy vs. Height')
plt.xlabel('Height (m)')
plt.ylabel('Potential Energy (J)')
plt.grid(True)
plt.show()