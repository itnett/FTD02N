python
import matplotlib.pyplot as plt

# Initiale betingelser
mass = 10  # kg
velocity = [0, 5, 10, 15, 20]  # m/s
height = 10  # meter
g = 9.81  # gravitasjonsakselerasjon

# Beregn kinetisk og potensiell energi
kinetic_energy = [0.5 * mass * v**2 for v in velocity]
potential_energy = [mass * g * height for _ in velocity]

plt.plot(velocity, kinetic_energy, label='Kinetisk Energi (J)')
plt.plot(velocity, potential_energy, label='Potensiell Energi (J)', linestyle='--')
plt.title("Kinetisk og Potensiell Energi")
plt.xlabel("Hastighet (m/s)")
plt.ylabel("Energi (J)")
plt.legend()
plt.show()