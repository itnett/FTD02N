python
import matplotlib.pyplot as plt

# Energibevaring: Kinetisk + Potensiell
mass = 1  # kg
heights = [0, 2, 4, 6, 8, 10]  # meter
g = 9.81  # m/s^2
velocities = [10, 8, 6, 4, 2, 0]  # m/s

# Beregne energier
kinetic_energy = [0.5 * mass * v**2 for v in velocities]
potential_energy = [mass * g * h for h in heights]
total_energy = [ke + pe for ke, pe in zip(kinetic_energy, potential_energy)]

plt.plot(heights, kinetic_energy, label='Kinetisk Energi')
plt.plot(heights, potential_energy, label='Potensiell Energi')
plt.plot(heights, total_energy, label='Total Energi', linestyle='--')
plt.title("Energibevaring")
plt.xlabel("Høyde (m)")
plt.ylabel("Energi (J)")
plt.legend()
plt.show()