python
# Trinket-kode for Leksjon 8.9: Gjennomsnittlig vekstfart

def average_growth_rate(y0, y1, t0, t1):
    return (y1 - y0) / (t1 - t0)

# Eksempelbruk
print("Leksjon 8.9: Gjennomsnittlig vekstfart")
y0 = float(input("Skriv inn startverdien (y0): "))
y1 = float(input("Skriv inn sluttverdien (y1): "))
t0 = float(input("Skriv inn starttidspunktet (t0): "))
t1 = float(input("Skriv inn sluttidspunktet (t1): "))
growth_rate = average_growth_rate(y0, y1, t0, t1)
print(f"Gjennomsnittlig vekstfart fra {t0} til {t1} er {growth_rate} per tidsenhet")

# Tegn vekstkurven
import matplotlib.pyplot as plt
import numpy as np

t_values = np.linspace(t0, t1, 400)
y_values = y0 + growth_rate * (t_values - t0)

plt.plot(t_values, y_values, label=f'Gjennomsnittlig vekstfart: {growth_rate:.2f}')
plt.scatter([t0, t1], [y0, y1], color='red')  # Start- og sluttverdier
plt.title('Gjennomsnittlig vekstfart')
plt.xlabel('Tid')
plt.ylabel('Verdi')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()