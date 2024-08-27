python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sympy as sp

# Funksjon for rett linje
def linje(x, m, c):
    return m * x + c

# Data for rett linje
x_data = np.linspace(0, 10, 100)
y_data = linje(x_data, 2, 5)

# Polynomfunksjon og dens deriverte
x = sp.symbols('x')
polynom = 3*x**2 + 2*x + 1
derivert_polynom = sp.diff(polynom, x)

# Eksponentialfunksjon
def eksponential(x, a, b):
    return a * np.exp(b * x)

# Data for eksponentialfunksjon
y_data_eksponential = eksponential(x_data, 1, 0.3)

# Eksempel på regresjon
# Generer syntetiske data
np.random.seed(0)
x_reg = np.linspace(0, 4, 50)
y_reg = linje(x_reg, 2, 3) + np.random.normal(size=x_reg.size)

# Utfør lineær regresjon
popt, pcov = curve_fit(linje, x_reg, y_reg)
m_fit, c_fit = popt

# Plotting
plt.figure(figsize=(10, 8))

# Plot for rett linje
plt.subplot(2, 2, 1)
plt.plot(x_data, y_data, label='y = 2x + 5')
plt.title('Rett Linje')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Plot for polynomfunksjon
plt.subplot(2, 2, 2)
x_vals = np.linspace(-3, 3, 100)
y_vals = [polynom.subs(x, val) for val in x_vals]
y_vals_derivert = [derivert_polynom.subs(x, val) for val in x_vals]
plt.plot(x_vals, y_vals, label='Polynom: 3x^2 + 2x + 1')
plt.plot(x_vals, y_vals_derivert, label='Derivert: 6x + 2')
plt.title('Polynomfunksjon og Derivert')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Plot for eksponentialfunksjon
plt.subplot(2, 2, 3)
plt.plot(x_data, y_data_eksponential, label='y = e^(0.3x)')
plt.title('Eksponentialfunksjon')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Plot for regresjon
plt.subplot(2, 2, 4)
plt.scatter(x_reg, y_reg, label='Data')
plt.plot(x_reg, linje(x_reg, m_fit, c_fit), label=f'Fit: y = {m_fit:.2f}x + {c_fit:.2f}', color='red')
plt.title('Lineær Regresjon')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()