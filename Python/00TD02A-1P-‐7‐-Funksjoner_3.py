python
# Trinket-kode for Leksjon 7.5: Funksjoner i Hverdagen

def kostnad(x):
    return 50*x + 200

# Eksempelbruk
print("Leksjon 7.5: Funksjoner i Hverdagen")
x = int(input("Skriv inn antall enheter: "))
print(f"Kostnaden for å produsere {x} enheter er {kostnad(x)} kroner.")

# Tegn grafen til kostnadsfunksjonen
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0, 20, 100)
y_values = kostnad(x_values)

plt.plot(x_values, y_values, label='C(x) = 50x + 200')
plt.title('Grafen til kostnadsfunksjonen C(x) = 50x + 200')
plt.xlabel('Antall enheter (x)')
plt.ylabel('Kostnad (C(x))')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()