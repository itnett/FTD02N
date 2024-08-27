python
# Trinket-kode for Leksjon 2: Bevegelseslikninger

# Funksjoner for bevegelseslikninger
def konstant_fart(distance, time):
    return distance / time

def konstant_akselerasjon(start_velocity, acceleration, time):
    return start_velocity + acceleration * time

def tilbakelagt_avstand(start_velocity, acceleration, time):
    return start_velocity * time + 0.5 * acceleration * time**2

# Eksempelbruk
print("Leksjon 2: Bevegelseslikninger")
distance = float(input("Skriv inn avstanden (m): "))
time = float(input("Skriv inn tiden (s): "))
fart = konstant_fart(distance, time)
print(f"Fart ved konstant fart: {fart} m/s")

start_velocity = float(input("Skriv inn startfarten (m/s): "))
acceleration = float(input("Skriv inn akselerasjonen (m/s^2): "))
time = float(input("Skriv inn tiden (s): "))
sluttfart = konstant_akselerasjon(start_velocity, acceleration, time)
print(f"Sluttfart ved konstant akselerasjon: {sluttfart} m/s")

# Tegn grafen for bevegelse ved konstant akselerasjon
import matplotlib.pyplot as plt
import numpy as np

times = np.linspace(0, 10, 100)
distances = tilbakelagt_avstand(start_velocity, acceleration, times)

plt.plot(times, distances, label=f'a = {acceleration} m/s^2')
plt.title('Bevegelse ved konstant akselerasjon')
plt.xlabel('Tid (s)')
plt.ylabel('Avstand (m)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()