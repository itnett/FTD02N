python
# Trinket-kode for Leksjon 1: Anvende Newtons Lover

# Funksjon for å beregne akselerasjon basert på Newtons andre lov
def newtons_second_law(force, mass):
    return force / mass

# Eksempelbruk
print("Leksjon 1: Anvende Newtons Lover")
mass = float(input("Skriv inn massen til objektet (kg): "))
force = float(input("Skriv inn kraften som virker på objektet (N): "))
acceleration = newtons_second_law(force, mass)
print(f"Akselerasjonen til objektet med masse {mass} kg og kraft {force} N er {acceleration} m/s^2")

# Tegn grafen for kraft vs akselerasjon
import matplotlib.pyplot as plt
import numpy as np

forces = np.linspace(0, 100, 100)
accelerations = newtons_second_law(forces, mass)

plt.plot(forces, accelerations, label=f'mass = {mass} kg')
plt.title('Newtons andre lov: Kraft vs Akselerasjon')
plt.xlabel('Kraft (N)')
plt.ylabel('Akselerasjon (m/s^2)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()