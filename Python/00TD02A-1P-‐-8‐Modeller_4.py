python
# Trinket-kode for Leksjon 8.5: Potensfunksjoner

def power_function(x):
    return 2 * x**3

# Eksempelbruk
print("Leksjon 8.5: Potensfunksjoner")
x = float(input("Skriv inn verdien av x: "))
print(f"f({x}) = 2 * {x}^3 = {power_function(x)}")

# Tegn grafen til potensfunksjonen
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0, 5, 400)
y_values = power_function(x_values)

plt.plot(x_values, y_values, label='f(x) = 2x^3')
plt.title('Grafen til potensfunksjonen f(x) = 2x^3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()