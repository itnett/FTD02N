python
# Trinket-kode for Leksjon 1: Algebra

# Funksjon for å lage et algebraisk uttrykk
def algebra_expression(x):
    return 2 * x + 3

# Eksempelbruk
print("Leksjon 1: Algebra")
x = float(input("Skriv inn verdien av x: "))
print(f"Algebraisk uttrykk 2x + 3 for x = {x} er {algebra_expression(x)}")

# Tegn grafen til det algebraiske uttrykket
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-10, 10, 400)
y_values = algebra_expression(x_values)

plt.plot(x_values, y_values, label='2x + 3')
plt.title('Grafen til det algebraiske uttrykket 2x + 3')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()