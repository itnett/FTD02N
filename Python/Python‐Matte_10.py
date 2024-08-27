python
import numpy as np

def solve_linear_system(a1=1, b1=2, c1=3, a2=4, b2=5, c2=6):
    """
    Solve a system of linear equations:
    a1*x + b1*y = c1
    a2*x + b2*y = c2
    
    Parameters:
    a1, b1, c1, a2, b2, c2 (float): Coefficients of the equations.
    
    Returns:
    tuple: Solutions for x and y.
    """
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    
    solutions = np.linalg.solve(A, B)
    x, y = solutions[0], solutions[1]
    
    print(f"Løsning: x = {x}, y = {y}")
    print(f"GeoGebra input: Solve[{a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}]")
    
    return x, y

# Example usage
solve_linear_system()