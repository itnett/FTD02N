python
import matplotlib.pyplot as plt

# Innsamlede data
lengder = [0.5, 1.0, 1.5]  # Lengder i meter
svingetider = [1.42, 2.01, 2.46]  # Svingetider i sekunder

# Beregn T^2 for hver svingetid
T_kvadrat = [T**2 for T in svingetider]

# Plot T^2 mot l
plt.plot(lengder, T_kvadrat, 'o', label='Eksperimentelle data')

# Tilpass en rett linje gjennom origo
koeffisienter = np.polyfit(lengder, T_kvadrat, 1)
linje = np.poly1d(koeffisienter)
plt.plot(lengder, linje(lengder), label=f'Lineær tilpasning: y = {koeffisienter[0]:.2f}x + {koeffisienter[1]:.2f}')

# Konfigurer plottet
plt.xlabel('Lengde (m)')
plt.ylabel('T^2 (s^2)')
plt.legend()
plt.title('Sammenhengen mellom T^2 og l')
plt.grid(True)

# Vis plottet
plt.show()