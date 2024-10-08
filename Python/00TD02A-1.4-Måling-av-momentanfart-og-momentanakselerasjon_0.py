python
import matplotlib.pyplot as plt

# Simulerte data (du vil erstatte disse med faktiske målinger)
tykkelse_stav = 0.005  # Meter (5 mm)
tidspunkt1 = [0.1, 0.2]  # Sekunder (når hver stav bryter første fotoport)
tidspunkt2 = [0.3, 0.5]  # Sekunder (når hver stav bryter andre fotoport)

# Beregninger
hastigheter = []
for i in range(2):
    delta_t = tidspunkt2[i] - tidspunkt1[i]
    hastigheter.append(tykkelse_stav / delta_t)

akselerasjon = (hastigheter[1] - hastigheter[0]) / (tidspunkt2[0] - tidspunkt1[0])

# Utskrift av resultater
print(f"Hastighet ved første fotoport: {hastigheter[0]:.2f} m/s")
print(f"Hastighet ved andre fotoport: {hastigheter[1]:.2f} m/s")
print(f"Gjennomsnittlig akselerasjon: {akselerasjon:.2f} m/s²")

# Plotting av hastigheter over tid
plt.plot(tidspunkt1, hastigheter, marker='o')
plt.xlabel('Tid (s)')
plt.ylabel('Hastighet (m/s)')
plt.title('Hastighet vs. Tid')
plt.grid(True)
plt.show()