python
# Trinket-kode for Leksjon 7.10: Egenskaper ved Andregradsfunksjoner

def f(x):
    return -x**2 + 6*x - 5

# Eksempelbruk
print("Leksjon 7.10: Egenskaper ved Andregradsfunksjoner")
x = float(input("Skriv inn verdien av x: "))
print(f"f({x}) = {f(x)}")

# Tegn grafen til funksjonen f(x)
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-10, 10, 400)
y_values = f(x_values)

plt.plot(x_values, y_values, label='f(x) = -x^2 + 6x - 5')
plt.title('Grafen til funksjonen f(x) = -x^2 + 6x - 5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()