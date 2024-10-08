python
import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic_inequality():
    print("Dette programmet løser og illustrerer andregradsulikheter på formen ax^2 + bx + c < 0.")
    
    a = float(input("Skriv inn konstanten a: "))
    b = float(input("Skriv inn konstanten b: "))
    c = float(input("Skriv inn konstanten c: "))
    
    D = b**2 - 4*a*c
    
    if D < 0:
        print("Ingen reelle røtter. Hvis a > 0, er funksjonen alltid større enn 0. Hvis a < 0, er funksjonen alltid mindre enn 0.")
    else:
        x1 = (-b + np.sqrt(D)) / (2*a)
        x2 = (-b - np.sqrt(D)) / (2*a)
        print(f"Nullpunktene er x1 = {x1} og x2 = {x2}")
    
    x = np.linspace(x1-1, x2+1, 400)
    y = a*x**2 + b*x + c
    
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(x1, color='red', linestyle='--')
    plt.axvline(x2, color='red', linestyle='--')
    plt.fill_between(x, y, where=(y < 0), color='gray', alpha=0.5)
    plt.legend()
    plt.title('Løsning av andregradsulikheter')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

plot_quadratic_inequality()