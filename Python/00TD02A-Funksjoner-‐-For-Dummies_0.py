python
# Trinket-kode for Leksjon 1: Rette linjer

import matplotlib.pyplot as plt
import numpy as np

# Definer en funksjon for å beregne y-verdiene til en rett linje
def linear_function(x, m, b):
    return m * x + b

# Eksempelbruk: y = 2x + 3
m = 2  # Stigningstallet
b = 3  # Konstantleddet

# Lag x-verdier fra -10 til 10
x_values = np.linspace(-10, 10, 100)
# Beregn y-verdiene ved hjelp av funksjonen
y_values = linear_function(x_values, m, b)

# Tegn grafen
plt.plot(x_values, y_values, label=f'y = {m}x + {b}')
plt.title('Rett Linje: y = 2x + 3')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Numerisk output for et gitt punkt
x = 5
y = linear_function(x, m, b)
print(f"For x = {x}, y = {y} for linjen y = {m}x + {b}")