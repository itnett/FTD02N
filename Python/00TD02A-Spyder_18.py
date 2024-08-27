python
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def f(x):
    return x**2  # Funksjonen vi vil integrere

a = 0  # Nedre grense
b = 1  # Øvre grense

resultat, feil = integrate.quad(f, a, b)
print(f"Integralet av f(x) = x^2 fra {a} til {b} er: {resultat:.4f}")

# Visualisering
x = np.linspace(a, b, 100)
y = f(x)
plt.plot(x, y)
plt.fill_between(x, y, alpha=0.2)  # Fyll området under grafen
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Numerisk integrasjon')
plt.show()