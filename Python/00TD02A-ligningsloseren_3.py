python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def solve_first_order_ode():
    t = sp.symbols('t')
    y = sp.Function('y')(t)
    
    ode = sp.Eq(sp.diff(y, t), t*y)
    ySol = sp.dsolve(ode)
    print("Løsning for første ordens differensiallikning:")
    sp.pretty_print(ySol)

    # Initialbetingelse
    cond = sp.Eq(y.subs(t, 0), 2)
    ySol_cond = sp.dsolve(ode, ics={y.subs(t, 0): 2})
    print("Løsning med initialbetingelse y(0) = 2:")
    sp.pretty_print(ySol_cond)

def solve_nonlinear_ode():
    t = sp.symbols('t')
    y = sp.Function('y')(t)
    
    ode = sp.Eq((sp.diff(y, t) + y)**2, 1)
    ySol = sp.dsolve(ode)
    print("Løsning for ikke-lineær differensiallikning:")
    sp.pretty_print(ySol)

    # Initialbetingelse
    cond = sp.Eq(y.subs(t, 0), 0)
    ySol_cond = sp.dsolve(ode, ics={y.subs(t, 0): 0})
    print("Løsning med initialbetingelse y(0) = 0:")
    sp.pretty_print(ySol_cond)

def solve_second_order_ode():
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    Dy = y.diff(x)

    ode = sp.Eq(y.diff(x, 2), sp.cos(2*x) - y)
    cond1 = sp.Eq(y.subs(x, 0), 1)
    cond2 = sp.Eq(Dy.subs(x, 0), 0)
    ySol = sp.dsolve(ode, ics={y.subs(x, 0): 1, Dy.subs(x, 0): 0})
    ySol = sp.simplify(ySol)
    print("Løsning for andre ordens differensiallikning med initialbetingelser:")
    sp.pretty_print(ySol)

def solve_third_order_ode():
    x = sp.symbols('x')
    u = sp.Function('u')(x)
    Du = u.diff(x)
    D2u = u.diff(x, 2)

    ode = sp.Eq(u.diff(x, 3), u)
    cond1 = sp.Eq(u.subs(x, 0), 1)
    cond2 = sp.Eq(Du.subs(x, 0), -1)
    cond3 = sp.Eq(D2u.subs(x, 0), sp.pi)
    uSol = sp.dsolve(ode, ics={u.subs(x, 0): 1, Du.subs(x, 0): -1, D2u.subs(x, 0): sp.pi})
    print("Løsning for tredje ordens differensiallikning med initialbetingelser:")
    sp.pretty_print(uSol)

def main():
    print("Løsning av differensiallikninger med SymPy")
    
    # Første ordens differensiallikning
    solve_first_order_ode()
    
    # Ikke-lineær differensiallikning
    solve_nonlinear_ode()
    
    # Andre ordens differensiallikning med initialbetingelser
    solve_second_order_ode()
    
    # Tredje ordens differensiallikning med initialbetingelser
    solve_third_order_ode()

if __name__ == "__main__":
    main()