python
# Fysikk - Newtons andre lov
# Beregner kraften gitt masse og akselerasjon

def calculate_force(mass, acceleration):
    return mass * acceleration

# Input
mass = float(input("Skriv inn massen (kg): "))
acceleration = float(input("Skriv inn akselerasjonen (m/s^2): "))

# Calculate and output
force = calculate_force(mass, acceleration)
print(f"Kraften er: {force} N")