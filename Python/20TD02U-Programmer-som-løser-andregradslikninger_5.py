python
# Løse lineære ligninger på formen ax + b = 0

# Importere nødvendige bibliotek
import ipywidgets as widgets
from IPython.display import display

def solve_linear(a, b):
    if a != 0:
        x = -b / a
        return f"Løsningen er x = {x}."
    else:
        if b == 0:
            return "Uendelig mange løsninger."
        else:
            return "Ingen løsninger."

# Interaktive widgets for input
a_slider = widgets.FloatText(description='Konstant a:', value=1)
b_slider = widgets.FloatText(description='Konstant b:', value=0)
output = widgets.Output()

def on_value_change(change):
    with output:
        output.clear_output()
        a = a_slider.value
        b = b_slider.value
        result = solve_linear(a, b)
        print(result)

a_slider.observe(on_value_change, names='value')
b_slider.observe(on_value_change, names='value')

display(a_slider, b_slider, output)