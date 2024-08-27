python
# Importere nødvendige biblioteker
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Definere funksjonen f(x)
def f(x):
    return x**2 + 2

# Beregne gjennomsnittlig vekstfart
def average_rate_of_change(f, x1, x2):
    return (f(x2) - f(x1)) / (x2 - x1)

# Beregne momentan vekstfart ved numerisk derivasjon
def instantaneous_rate_of_change(f, x, delta_x):
    return (f(x + delta_x) - f(x)) / delta_x

# Widgets for brukerinput
x1_input = widgets.FloatText(description='x1:', value=0)
x2_input = widgets.FloatText(description='x2:', value=1)
x_input = widgets.FloatText(description='x:', value=0.5)
delta_x_input = widgets.FloatText(description='Delta x:', value=0.1)
output = widgets.Output()

def on_value_change(change):
    with output:
        output.clear_output()
        x1 = x1_input.value
        x2 = x2_input.value
        x = x_input.value
        delta_x = delta_x_input.value
        avg_rate = average_rate_of_change(f, x1, x2)
        inst_rate = instantaneous_rate_of_change(f, x, delta_x)
        print(f"Gjennomsnittlig vekstfart mellom x = {x1} og x = {x2}: {avg_rate:.5f}")
        print(f"Momentan vekstfart ved x = {x} (delta x = {delta_x}): {inst_rate:.5f}")

x1_input.observe(on_value_change, names='value')
x2_input.observe(on_value_change, names='value')
x_input.observe(on_value_change, names='value')
delta_x_input.observe(on_value_change, names='value')

display(x1_input, x2_input, x_input, delta_x_input, output)