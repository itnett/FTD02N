python
# KE35: Matematisk teori og kunnskapsområder

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

x = sp.symbols('x')

def plot_function(expression_str):
    expression = sp.sympify(expression_str)
    f = sp.lambdify(x, expression, 'numpy')
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {expression}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title('Plot av funksjonen')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

# Widget for funksjonsinnputt
function_input = widgets.Text(description='Funksjon:', placeholder='Skriv inn en funksjon av x')
output = widgets.Output()

def on_function_change(change):
    with output:
        output.clear_output(wait=True)
        expression_str = function_input.value
        plot_function(expression_str)

function_input.observe(on_function_change, names='value')

display(function_input, output)