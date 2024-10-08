python
# Trinket-kode for Leksjon 1: Beregne Arbeid, Effekt og Virkningsgrad

# Funksjon for å beregne arbeid
def calculate_work(force, distance):
    return force * distance

# Funksjon for å beregne effekt
def calculate_power(work, time):
    return work / time

# Funksjon for å beregne virkningsgrad
def calculate_efficiency(output_power, input_power):
    return (output_power / input_power) * 100

# Eksempelbruk
print("Leksjon 1: Beregne Arbeid, Effekt og Virkningsgrad")

force = float(input("Skriv inn kraften som virker på objektet (N): "))
distance = float(input("Skriv inn avstanden objektet flyttes (m): "))
work = calculate_work(force, distance)
print(f"Arbeid utført: {work} J")

time = float(input("Skriv inn tiden arbeidet utføres på (s): "))
power = calculate_power(work, time)
print(f"Effekt: {power} W")

input_power = float(input("Skriv inn input effekt (W): "))
output_power = float(input("Skriv inn output effekt (W): "))
efficiency = calculate_efficiency(output_power, input_power)
print(f"Virkningsgrad: {efficiency}%")

# Tegn grafen for arbeid vs avstand
import matplotlib.pyplot as plt
import numpy as np

distances = np.linspace(0, 10, 100)
works = calculate_work(force, distances)

plt.plot(distances, works, label=f'force = {force} N')
plt.title('Arbeid vs Avstand')
plt.xlabel('Avstand (m)')
plt.ylabel('Arbeid (J)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()