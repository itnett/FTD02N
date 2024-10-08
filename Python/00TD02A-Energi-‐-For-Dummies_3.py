python
# Trinket-kode for Leksjon 4: Termodynamikkens Første Lov

# Funksjon for å beregne endring i indre energi
def calculate_internal_energy_change(heat, work):
    return heat - work

# Eksempelbruk
print("Leksjon 4: Termodynamikkens Første Lov")

heat = float(input("Skriv inn varmen tilført systemet (J): "))
work = float(input("Skriv inn arbeidet utført av systemet (J): "))
internal_energy_change = calculate_internal_energy_change(heat, work)
print(f"Endring i indre energi: {internal_energy_change} J")

# Tegn grafen for indre energiendring vs tilført varme
import matplotlib.pyplot as plt
import numpy as np

heats = np.linspace(0, 1000, 100)
internal_energy_changes = calculate_internal_energy_change(heats, work)

plt.plot(heats, internal_energy_changes, label=f'work = {work} J')
plt.title('Indre Energiendring vs Tilført Varme')
plt.xlabel('Tilført Varme (J)')
plt.ylabel('Indre Energiendring (J)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()