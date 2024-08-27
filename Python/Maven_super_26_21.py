python
import pdb

def feilaktig_funksjon(a, b):
    pdb.set_trace()  # Starter en debugging session her
    return a / b

feilaktig_funksjon(10, 0)  # Dette vil kaste en ZeroDivisionError