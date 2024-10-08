python
# Beregn kinetisk energi (Ek = 0.5 * m * v^2)
def kinetisk_energi(masse, fart):
    return 0.5 * masse * fart**2

# Beregn potensiell energi (Ep = m * g * h)
def potensiell_energi(masse, høyde, gravitasjon=9.81):
    return masse * gravitasjon * høyde

# Eksempel: masse = 10 kg, fart = 5 m/s, høyde = 10 m
masse = 10
fart = 5
høyde = 10

print(f"Kinetisk energi: {kinetisk_energi(masse, fart)} J")
print(f"Potensiell energi: {potensiell_energi(masse, høyde)} J")