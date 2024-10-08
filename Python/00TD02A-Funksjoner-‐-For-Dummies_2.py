python
# Trinket-kode for Leksjon 3: Eksponentialfunksjoner

import matplotlib.pyplot as plt
import numpy as np

# Definer en funksjon for å beregne y-verdiene til en eksponentialfunksjon
def exponential_function(x, a, b):
    return a * b**x

# Eksempelbruk: y = 2 * 3^x
a = 2  # Startverdien
b = 3  # Vekstfaktoren

# Lag x-verdier fra -2 til 2
x_values = np.linspace(-2, 2, 100)
# Beregn y-verdiene ved hjelp av funksjonen
y_values = exponential_function(x_values, a, b)

# Tegn grafen
plt.plot(x_values, y_values, label=f'y = {a} * {b}^x')
plt.title('Eksponentialfunksjon: y = 2 * 3^x')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Numerisk output for et gitt punkt
x = 2
y = exponential_function(x, a, b)
print(f"For x = {x}, y = {y} for eksponentialfunksjonen y = {a} * {b}^x")