python
# Importere nødvendige biblioteker
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definere en funksjon for et polynom
def polynomial_function(coefficients):
    x = sp.symbols('x')
    f = sum(c*x**i for i, c in enumerate(coefficients))
    return f

# Finne røttene til funksjonen
def find_roots(f):
    x = sp.symbols('x')
    roots = sp.solve(f, x)
    return roots

# Finne ekstremalpunkter
def find_extrema(f):
    x = sp.symbols('x')
    f_prime = sp.diff(f, x)
    critical

_points = sp.solve(f_prime, x)
    return critical_points, f_prime

# Tegne grafen til funksjonen
def plot_polynomial(coefficients):
    x_vals = np.linspace(-10, 10, 400)
    x = sp.symbols('x')
    f = polynomial_function(coefficients)
    f_lambdified = sp.lambdify(x, f, 'numpy')
    y_vals = f_lambdified(x_vals)
    
    roots = find_roots(f)
    critical_points, f_prime = find_extrema(f)
    f_prime_lambdified = sp.lambdify(x, f_prime, 'numpy')
    y_prime_vals = f_prime_lambdified(x_vals)
    
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.plot(x_vals, y_prime_vals, label="f'(x)", linestyle='--')
    for root in roots:
        plt.plot(root, f_lambdified(root), 'ro', label=f'Root: x={root:.2f}')
    for cp in critical_points:
        plt.plot(cp, f_lambdified(cp), 'go', label=f'Critical Point: x={cp:.2f}')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title('Polynomfunksjon og dens deriverte')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Hovedprogram for polynomfunksjoner
def polynomial_main():
    print("Dette programmet drøfter en vilkårlig polynomfunksjon av valgfri grad.")
    
    user_input = input("Skriv inn koeffisientene til polynomfunksjonen separert med mellomrom (start med den laveste graden): ")
    coefficients = list(map(float, user_input.split()))
    
    plot_polynomial(coefficients)

# Kjøre hovedprogrammet
polynomial_main()