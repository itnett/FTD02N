python
# Trinket-kode for Leksjon 2: Beregne Kinetisk og Potensiell Energi

# Funksjon for å beregne kinetisk energi
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

# Funksjon for å beregne potensiell energi
def calculate_potential_energy(mass, height, gravity=9.81):
    return mass * gravity * height

# Eksempelbruk
print("Leksjon 2: Beregne Kinetisk og Potensiell Energi")

mass = float(input("Skriv inn massen til objektet (kg): "))
velocity = float(input("Skriv inn farten til objektet (m/s): "))
kinetic_energy = calculate_kinetic_energy(mass, velocity)
print(f"Kinetisk energi: {kinetic_energy} J")

height = float(input("Skriv inn høyden til objektet over bakken (m): "))
potential_energy = calculate_potential_energy(mass, height)
print(f"Potensiell energi: {potential_energy} J")

# Tegn grafen for kinetisk energi vs fart
import matplotlib.pyplot as plt
import numpy as np

velocities = np.linspace(0, 10, 100)
kinetic_energies = calculate_kinetic_energy(mass, velocities)

plt.plot(velocities, kinetic_energies, label=f'mass = {mass} kg')
plt.title('Kinetisk Energi vs Fart')
plt.xlabel('Fart (m/s)')
plt.ylabel('Kinetisk Energi (J)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()