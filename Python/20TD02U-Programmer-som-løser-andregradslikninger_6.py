python
# Løse et system av to lineære ligninger

import numpy as np
import ipywidgets as widgets
from IPython.display import display

def solve_linear_system(a, b, e, c, d, f):
    A = np.array([[a, b], [c, d]])
    B = np.array([e, f])
    try:
        solution = np.linalg.solve(A, B)
        return f"Løsningen er x = {solution[0]}, y = {solution[1]}"
    except np.linalg.LinAlgError:
        return "Ligningssystemet har ingen unik løsning."

# Interaktive widgets for input
a_slider = widgets.FloatText(description='Konstant a:', value=1)
b_slider = widgets.FloatText(description='Konstant b:', value=1)
e_slider = widgets.FloatText(description='Konstant e:', value=1)
c_slider = widgets.FloatText(description='Konstant c:', value=1)
d_slider = widgets.FloatText(description='Konstant d:', value=1)
f_slider = widgets.FloatText(description='Konstant f:', value=1)
output = widgets.Output()

def on_value_change(change):
    with output:
        output.clear_output()
        a = a_slider.value
        b = b_slider.value
        e = e_slider.value
        c = c_slider.value
        d = d_slider.value
        f = f_slider.value
        result = solve_linear_system(a, b, e, c, d, f)
        print(result)

a_slider.observe(on_value_change, names='value')
b_slider.observe(on_value_change, names='value')
e_slider.observe(on_value_change, names='value')
c_slider.observe(on_value_change, names='value')
d_slider.observe(on_value_change, names='value')
f_slider.observe(on_value_change, names='value')

display(a_slider, b_slider, e_slider, c_slider, d_slider, f_slider, output)