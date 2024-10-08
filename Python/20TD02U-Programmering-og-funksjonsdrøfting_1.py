python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, diff

# Definere funksjonen og den deriverte
def cubic_function(a, b, c, d):
    x = symbols('x')
    f = a*x**3 + b*x**2 + c*x + d
    f_prime = diff(f, x)
    return f, f_prime

# Drøfte monotoniegenskaper
def monotonicity(f_prime):
    x = symbols('x')
    critical_points = solve(Eq(f_prime, 0), x)
    return critical_points

# Finne nullpunkter
def find_roots(a, b, c, d):
    x = symbols('x')
    f = a*x**3 + b*x**2 + c*x + d
    roots = solve(Eq(f, 0), x)
    return roots

# Finne toppunkt/bunnpunkt
def find_extremum(f_prime):
    x = symbols('x')
    critical_points = solve(Eq(f_prime, 0), x)
    return critical_points

# Finne skjæringspunkt med y-aksen
def y_intercept(d):
    return d

# Tegne grafen
def plot_cubic(a, b, c, d):
    x = np.linspace(-10, 10, 400)
    y = a*x**3 + b*x**2 + c*x + d
    plt.plot(x, y, label=f'{a}x^3 + {b}x^2 + {c}x + {d}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title('Tredjegradsfunksjon')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

# Hovedprogram
def main():
    print("Dette programmet gjør funksjonsdrøfting av en vilkårlig tredjegradsfunksjon.")
    
    user_input = input("Skriv inn verdiene for a, b, c og d separert med mellomrom: ")
    a, b, c, d = map(float, user_input.split())
    
    f, f_prime = cubic_function(a, b, c, d)
    print(f"Den deriverte funksjonen: f'(x) = {f_prime}")
    
    critical_points = monotonicity(f_prime)
    print(f"Monotoniegenskaper: Kritiske punkter: {critical_points}")
    
    roots = find_roots(a, b, c, d)
    print(f"Nullpunkter: {roots}")
    
    extremum = find_extremum(f_prime)
    print(f"Toppunkt/bunnpunkt: {extremum}")
    
    y_int = y_intercept(d)
    print(f"Skjæringspunkt med y-aksen: (0, {y_int})")
    
    plot_cubic(a, b, c, d)

main()