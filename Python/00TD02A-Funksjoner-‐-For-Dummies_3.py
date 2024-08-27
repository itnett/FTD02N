python
# Trinket-kode for Leksjon 4: Derivasjon av Polynomfunksjoner

import sympy as sp

# Definer variabelen x
x = sp.symbols('x')

# Definer polynomfunksjonen
polynomial = 4*x**3 - 3*x**2 + 2*x - 1

# Finn den deriverte av polynomfunksjonen
derivative = sp.diff(polynomial, x)

# Vis den deriverte
print(f"Den deriverte av polynomet 4x^3 - 3x^2 + 2x - 1 er {derivative}")

# Numerisk beregning av den deriverte ved et gitt punkt
x_value = 1
slope = derivative.evalf(subs={x: x_value})
print(f"Hellingen på grafen til polynomet ved x = {x_value} er {slope}")

# Tegn grafen til polynomet og den deriverte
import numpy as np
import matplotlib.pyplot as plt

# Konverter sympy-funksjonen til en numpy-funksjon
f_polynomial = sp.lambdify(x, polynomial, 'numpy')
f_derivative = sp.lambdify(x, derivative, 'numpy')

# Lag x-verdier fra -2 til 2
x_values = np.linspace(-2, 2, 100)
# Beregn y-verdiene for polynomet og den deriverte
y_values_polynomial = f_polynomial(x_values)
y_values_derivative = f_derivative(x_values)

# Tegn grafene
plt.plot(x_values, y_values_polynomial, label='y = 4x^3 - 3x^2 + 2x - 1')
plt.plot(x_values, y_values_derivative, label="y' = 12x^2 - 6x + 2", linestyle='--')
plt.title('Polynom og dets Deriverte')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()