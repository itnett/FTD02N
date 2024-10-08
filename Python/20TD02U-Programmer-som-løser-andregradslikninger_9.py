python
# KE34: Abstraksjon og generalisering

import sympy as sp
import ipywidgets as widgets
from IPython.display import display

x = sp.symbols('x')

def generalize_expression(expression_str):
    expression = sp.sympify(expression_str)
    expanded_expr = sp.expand(expression)
    factored_expr = sp.factor(expression)
    return expanded_expr, factored_expr

# Widget for uttrykkinnputt
expression_input = widgets.Text(description='Uttrykk:', placeholder='Skriv inn et algebraisk uttrykk')
output = widgets.Output()

def on_expression_change(change):
    with output:
        output.clear_output()
        expression_str = expression_input.value
        expanded_expr, factored_expr = generalize_expression(expression_str)
        print(f"Utvidet uttrykk: {expanded_expr}")
        print(f"Faktorisert uttrykk: {factored_expr}")

expression_input.observe(on_expression_change, names='value')

display(expression_input, output)