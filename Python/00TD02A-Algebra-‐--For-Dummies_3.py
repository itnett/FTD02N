python
# Trinket-kode for Leksjon 4: Potenser

# Funksjon for å beregne potenser
def power(base, exponent):
    return base ** exponent

# Eksempelbruk
print("Leksjon 4: Potenser")
base = float(input("Skriv inn grunntallet: "))
exponent = float(input("Skriv inn eksponenten: "))
print(f"{base}^{exponent} = {power(base, exponent)}")

# Tegn grafen til potensfunksjoner
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0, 5, 400)
y_values = power(x_values, exponent)

plt.plot(x_values, y_values, label=f'{base}^{exponent}')
plt.title(f'Grafen til potensfunksjonen {base}^{exponent}')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()