python
# Trinket-kode for Leksjon 2: Polynomfunksjoner

import matplotlib.pyplot as plt
import numpy as np

# Definer en funksjon for å beregne y-verdiene til et polynom
def polynomial_function(x):
    return x**3 - 2*x**2 - x + 2

# Lag x-verdier fra -3 til 3
x_values = np.linspace(-3, 3, 100)
# Beregn y-verdiene ved hjelp av funksjonen
y_values = polynomial_function(x_values)

# Tegn grafen
plt.plot(x_values, y_values, label='y = x^3 - 2x^2 - x + 2')
plt.title('Polynomfunksjon: y = x^3 - 2x^2 - x + 2')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Numerisk output for et gitt punkt
x = 1
y = polynomial_function(x)
print(f"For x = {x}, y = {y} for polynomet y = x^3 - 2x^2 - x + 2")