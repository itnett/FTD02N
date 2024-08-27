python
# Utforske andregradsulikheter grafisk

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

def plot_quadratic_inequality(a, b, c):
    D = b**2 - 4*a*c
    
    x1 = (-b + np.sqrt(D)) / (2*a) if D >= 0 else None
    x2 = (-b - np.sqrt(D)) / (2*a) if D >= 0 else None
    
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.axhline(0, color='black', linewidth=0.5)
    if x1 is not None and x2 is not None:
        plt.axvline(x1, color='red', linestyle='--')
        plt.axvline(x2, color='red', linestyle='--')
        plt.fill_between(x, y, where=(y < 0), color='gray', alpha=0.5)
    plt.legend()
    plt.title('Løsning av andregradsulikheter')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Interaktive widgets for input
a_slider = widgets.FloatText(description='Konstant a:', value=1)
b_slider = widgets.FloatText(description='Konstant b:', value=0)
c_slider = widgets.FloatText(description='Konstant c:', value=0)
output = widgets.Output()

def on_value_change(change):
    with output:
        output.clear_output(wait=True)
        a = a_slider.value
        b = b_slider.value
        c = c_slider.value
        plot_quadratic_inequality(a, b, c)

a_slider.observe(on_value_change, names='value')
b_slider.observe(on_value_change, names='value')
c_slider.observe(on_value_change, names='value')

display(a_slider, b_slider, c_slider, output)