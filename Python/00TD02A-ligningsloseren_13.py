python
import sympy as sp

def solve_symbolic_equations():
    sp.init_printing()
    x, y, z = sp.symbols('x y z')
    c1 = sp.Symbol('c1')
    
    # Definer ligninger
    f = sp.Eq(2 * x**2 + y + z, 1)
    g = sp.Eq(x + 2 * y + z, c1)
    h = sp.Eq(-2 * x + y, -z)
    
    # Løs ligningene symbolsk
    solutions = sp.solve([f, g, h], (x, y, z))
    print("Symbolske løsninger for ligningssystemet:")
    sp.pretty_print(solutions)

solve_symbolic_equations()