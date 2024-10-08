python
# Trinket-kode for Leksjon 8.3: Polynomfunksjoner

def polynomial_function(x):
    return x**3 - 3*x**2 + 2*x

# Eksempelbruk
print("Leksjon 8.3: Polynomfunksjoner")
x = float(input("Skriv inn verdien av x: "))
print(f"P({x}) = {polynomial_function(x)}")

# Tegn grafen til polynomfunksjonen
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-3, 3, 400)
y_values = polynomial_function(x_values)

plt.plot(x_values, y_values, label='P(x) = x^3 - 3x^2 + 2x')
plt.title('Grafen til polynomfunksjonen P(x) = x^3 - 3x^2 + 2x')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()