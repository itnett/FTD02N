python
import numpy as np
import matplotlib.pyplot as plt

def draw_cubic_function():
    print("Dette programmet tegner funksjonen f(x) = ax^3 + bx^2 + cx + d for x-verdier i intervallet fra s til t.")
    
    a = float(input("Skriv inn verdien til konstanten a: "))
    b = float(input("Skriv inn verdien til konstanten b: "))
    c = float(input("Skriv inn verdien til konstanten c: "))
    d = float(input("Skriv inn verdien til konstanten d: "))
    s = float(input("Skriv inn verdien til konstanten s: "))
    t = float(input("Skriv inn verdien til konstanten t: "))
    
    x = np.linspace(s, t, 100)
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

draw_cubic_function()