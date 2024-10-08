python
from gekko import GEKKO

def solve_nonlinear_equations_gekko():
    m = GEKKO()
    x, y, w = [m.Var(1) for _ in range(3)]
    m.Equations([x**2 + y**2 == 20, y - x**2 == 0, w + 5 - x * y == 0])
    m.solve(disp=False)
    print("Løsning for ikke-lineære ligninger med GEKKO:", x.value, y.value, w.value)

solve_nonlinear_equations_gekko()