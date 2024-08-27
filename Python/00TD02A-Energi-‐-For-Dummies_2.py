python
# Trinket-kode for Leksjon 3: Anvende Energibevaring

# Funksjon for å beregne total energi
def calculate_total_energy(kinetic_energy, potential_energy):
    return kinetic_energy + potential_energy

# Eksempelbruk
print("Leksjon 3: Anvende Energibevaring")

mass = float(input("Skriv inn massen til objektet (kg): "))
height = float(input("Skriv inn høyden til objektet over bakken (m): "))
velocity = float(input("Skriv inn farten til objektet (m/s): "))

kinetic_energy = calculate_kinetic_energy(mass, velocity)
potential_energy = calculate_potential_energy(mass, height)
total_energy = calculate_total_energy(kinetic_energy, potential_energy)
print(f"Total energi: {total_energy} J")

# Tegn grafen for total energi vs høyde
import matplotlib.pyplot as plt
import numpy as np

heights = np.linspace(0, 10, 100)
potential_energies = calculate_potential_energy(mass, heights)
total_energies = calculate_total_energy(kinetic_energy, potential_energies)

plt.plot(heights, total_energies, label=f'mass = {mass} kg')
plt.title('Total Energi vs Høyde')
plt.xlabel('Høyde (m)')
plt.ylabel('Total Energi (J)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()