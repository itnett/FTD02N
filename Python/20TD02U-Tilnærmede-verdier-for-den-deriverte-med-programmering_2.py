python
import numpy as np
import matplotlib.pyplot as plt

def cubic_function(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

def derivative_approximation(f, x, delta_x):
    return (f(x + delta_x) - f(x)) / delta_x

def plot_cubic_function_and_derivative():
    print("Dette programmet tegner en vilkårlig tredjegradsfunksjon og beregner den deriverte ved x-verdier i et gitt intervall.")
    
    user_input = input("Skriv inn verdiene for a, b, c, d, s og t separert med mellomrom: ")
    a, b, c, d, s, t = map(float, user_input.split())
    
    x = np.linspace(s, t, 100)
    y = cubic_function(x, a, b, c, d)
    
    plt.plot(x, y, label=f'{a}x^3 + {b}x^2 + {c}x + {d}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title('Tredjegradsfunksjon')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

    x_value = float(input("Skriv inn verdien for x hvor du vil beregne den deriverte: "))
    delta_x = 0.1
    tolerance = 0.00001
    
    previous_derivative = derivative_approximation(lambda x: cubic_function(x, a, b, c, d), x_value, delta_x)
    delta_x /= 10
    current_derivative = derivative_approximation(lambda x: cubic_function(x, a, b, c, d), x_value, delta_x)

    while abs(current_derivative - previous_derivative) > tolerance:
        previous_derivative = current_derivative
        delta_x /= 10
        current_derivative = derivative_approximation(lambda x: cubic_function(x, a, b, c, d), x_value, delta_x)
    
    print(f"Den deriverte til funksjonen ved x = {x_value} er tilnærmet {current_derivative:.5f}")

plot_cubic_function_and_derivative()