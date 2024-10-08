python
# Energi - Kinetisk energi
# Beregner kinetisk energi gitt masse og fart

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

# Input
mass = float(input("Skriv inn massen (kg): "))
velocity = float(input("Skriv inn farten (m/s): "))

# Calculate and output
kinetic_energy = calculate_kinetic_energy(mass, velocity)
print(f"Kinetisk energi er: {kinetic_energy} J")