python
# KE30: Utforskning og problemløsing

import ipywidgets as widgets
from IPython.display import display

def find_pattern(sequence):
    differences = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return differences

# Widget for sekvensinnputt
sequence_input = widgets.Text(description='Sekvens:', placeholder='Skriv inn tall adskilt med komma')
output = widgets.Output()

def on_sequence_change(change):
    with output:
        output.clear_output()
        sequence = list(map(int, sequence_input.value.split(',')))
        differences = find_pattern(sequence)
        print(f"Differanser: {differences}")

sequence_input.observe(on_sequence_change, names='value')

display(sequence_input, output)