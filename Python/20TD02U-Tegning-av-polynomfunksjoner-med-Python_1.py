python
import numpy as np
import matplotlib.pyplot as plt

def draw_cubic_function():
    print("Dette programmet tegner funksjonen f(x) = ax^3 + bx^2 + cx + d for x-verdier i intervallet fra s til t.")
    
    user_input = input("Skriv inn verdiene til a, b, c, d, s og t separert med mellomrom: ")
    a, b, c, d, s, t = map(float, user_input.split())
    
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