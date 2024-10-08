python
# Trinket-kode for Leksjon 8.7: Eksponentialfunksjoner

def exponential_function(x):
    return 5 * 2**x

# Eksempelbruk
print("Leksjon 8.7: Eksponentialfunksjoner")
x = float(input("Skriv inn verdien av x: "))
print(f"f({x}) = 5 * 2^{x} = {exponential_function(x)}")

# Tegn grafen til eksponentialfunksjonen
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(

0, 5, 400)
y_values = exponential_function(x_values)

plt.plot(x_values, y_values, label='f(x) = 5 * 2^x')
plt.title('Grafen til eksponentialfunksjonen f(x) = 5 * 2^x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()