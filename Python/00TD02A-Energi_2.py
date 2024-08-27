python
# Simplified pendulum simulation
theta = np.linspace(0, 2*np.pi, 100)
length = 1.0  # m

# Calculate x and y positions for the pendulum bob
x = length * np.sin(theta)
y = -length * np.cos(theta)

# Plot the pendulum's motion
plt.figure(figsize=(8, 8))
plt.plot(x, y, marker='o', linestyle='-', color='red')
plt.title('Pendulum Motion')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid(True)
plt.axis('equal')  # Ensure equal scaling on both axes
plt.show()