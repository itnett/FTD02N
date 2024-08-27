python
# Trinket-kode for Leksjon 8.1: Lineære modeller

def linear_model(x):
    return 2 * x + 3

# Eksempelbruk
print("Leksjon 8.1: Lineære modeller")
x = float(input("Skriv inn verdien av x: "))
print(f"y = 2 * {x} + 3 = {linear_model(x)}")

# Tegn grafen til den lineære modellen
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-10, 10, 400)
y_values = linear_model(x_values)

plt.plot(x_values, y_values, label='y = 2x + 3')
plt.title('Grafen til den lineære modellen y = 2x + 3')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()