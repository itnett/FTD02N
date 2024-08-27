python
import numpy as np
from scipy.optimize import fsolve

def solve_redlich_kwong():
    # Konstantverdier
    TC = 77  # degC
    P = 1.0  # bar
    a = 2.877e8  # cm^6 bar K^0.5 / mol^2
    b = 60.211  # cm^3 / mol
    Rg = 83.144598  # cm^3 bar / K-mol
    TK = TC + 273.15  # K
    Vg = Rg * TK / P  # ideal gas guess
    
    # Definer funksjonen
    def f(V):
        return P - Rg * TK / (V - b) + a / (np.sqrt(TK) * V * (V + b))
    
    # Løs for dampvolum
    V = fsolve(f, Vg)
    print(f'Scipy løsning for dampvolum: {V[0]:0.1f} cm^3/mol')
    
    # Løs for væskevolum
    V = fsolve(f, b * 1.1)
    print(f'Scipy løsning for væskevolum: {V[0]:0.1f} cm^3/mol')

    # Løsning med GEKKO
    from gekko import GEKKO
    m = GEKKO(remote=False)
    V = m.Var(value=Vg, lb=1e4)
    m.Equation(P == Rg * TK / (V - b) - a / (np.sqrt(TK) * V * (V + b)))
    m.options.SOLVER = 1
    m.solve(disp=False)
    print(f'Gekko løsning for dampvolum: {V.value[0]:0.1f} cm^3/mol')
    
    # Oppdater grenser og startverdi
    V.lower = b * 0.5
    V.upper = b * 2
    V.value = b * 1.1
    m.options.SOLVER = 1
    m.solve(disp=False)
    print(f'Gekko løsning for væskevolum: {V.value[0]:0.1f} cm^3/mol')

solve_redlich_kwong()