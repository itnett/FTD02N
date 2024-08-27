python
import numpy as np

def solve_linear_equations():
    # Definer koeffisientmatriser og høyresidevektorer
    A = np.array([[3, -9], [2, 4]])
    b = np.array([-42, 2])
    
    # Løs lineære ligninger
    z = np.linalg.solve(A, b)
    print("Løsning for første sett av lineære ligninger:", z)
    
    M = np.array([[1, -2, -1], [2, 2, -1], [-1, -1, 2]])
    c = np.array([6, 1, 1])
    
    # Løs lineære ligninger
    y = np.linalg.solve(M, c)
    print("Løsning for andre sett av lineære ligninger:", y)

solve_linear_equations()