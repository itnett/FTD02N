python
import numpy as np
from scipy.optimize import fsolve

def solve_nonlinear_equations():
    def myFunction(z):
        x, y, w = z
        F = np.empty(3)
        F[0] = x**2 + y**2 - 20
        F[1] = y - x**2
        F[2] = w + 5 - x * y
        return F

    zGuess = np.array([1, 1, 1])
    z = fsolve(myFunction, zGuess)
    print("Løsning for ikke-lineære ligninger med fsolve:", z)

solve_nonlinear_equations()