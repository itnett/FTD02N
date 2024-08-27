python
import matplotlib.pyplot as plt
import numpy as np

def bacteria_growth(t, N0, r):
    return N0 * np.exp(r * t)

# Initiale betingelser
N0 = 100  # Initialt antall bakterier
r = 0.3   # Vekstrate per time
t = np.linspace(0, 24, 100)  # Tid fra 0 til 24 timer

# Beregn bakterieveksten
N = bacteria_growth(t, N0, r)

# Plot resultatene
plt.figure(figsize=(10, 6))
plt.plot(t, N, label='Bakterievekst')
plt.xlabel('Tid (timer)')
plt.ylabel('Antall bakterier')
plt.title('Modellering av bakterievekst over tid')
plt.legend()
plt.grid(True)
plt.show()