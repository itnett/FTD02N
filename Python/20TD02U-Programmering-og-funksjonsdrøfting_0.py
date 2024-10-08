python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, diff

# Definere funksjonen og den deriverte
def quadratic_function(a, b, c):
    x = symbols('x')
    f = a*x**2 + b*x + c
    f_prime = diff(f, x)
    return f, f_prime

# Drøfte monotoniegenskaper
def monotonicity(f_prime):
    x = symbols('x')
    critical_points = solve(Eq(f_prime, 0), x)
    return critical_points

# Finne nullpunkter
def find_roots(a, b, c):
    x = symbols('x')
    f = a*x**2 + b*x + c
    roots = solve(Eq(f, 0), x)
    return roots

# Finne toppunkt/bunnpunkt
def find_extremum(f_prime):
    x = symbols('x')
    critical_points = solve(Eq(f_prime, 0), x)
    return critical_points

# Finne skjæringspunkt med y-aksen
def y_intercept(a, b, c):
    return c

# Tegne grafen
def plot_quadratic(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title('Andregradsfunksjon')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

# Hovedprogram
def main():
    print("Dette programmet gjør funksjonsdrøfting av en vilkårlig andregradsfunksjon.")
    
    user_input = input("Skriv inn verdiene for a, b og c separert med mellomrom: ")
    a, b, c = map(float, user_input.split())
    
    f, f_prime = quadratic_function(a, b, c)
    print(f"Den deriverte funksjonen: f'(x) = {f_prime}")
    
    critical_points = monotonicity(f_prime)
    print(f"Monotoniegenskaper: Kritiske punkter: {critical_points}")
    
    roots = find_roots(a, b, c)
    print(f"Nullpunkter: {roots}")
    
    extremum = find_extremum(f_prime)
    print(f"Toppunkt/bunnpunkt: {extremum}")
    
    y_int = y_intercept(a, b, c)
    print(f"Skjæringspunkt med y-aksen: (0, {y_int})")
    
    plot_quadratic(a, b, c)

main()