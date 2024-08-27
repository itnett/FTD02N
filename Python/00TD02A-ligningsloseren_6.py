python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# SymPy Solutions

def plot_sympy_solution():
    t = sp.symbols('t')
    y = sp.Function('y')(t)
    
    # First order ODE
    ode1 = sp.Eq(sp.diff(y, t), t * y)
    ySol1 = sp.dsolve(ode1, ics={y.subs(t, 0): 2})
    ySol1 = sp.lambdify(t, ySol1.rhs, 'numpy')
    
    t_vals = np.linspace(0, 5, 100)
    y_vals1 = ySol1(t_vals)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t_vals, y_vals1, label="First Order ODE Solution")
    
    # Second order ODE
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    Dy = y.diff(x)
    ode2 = sp.Eq(y.diff(x, 2), sp.cos(2 * x) - y)
    ySol2 = sp.dsolve(ode2, ics={y.subs(x, 0): 1, Dy.subs(x, 0): 0})
    ySol2 = sp.lambdify(x, ySol2.rhs, 'numpy')
    
    x_vals = np.linspace(0, 5, 100)
    y_vals2 = ySol2(x_vals)
    
    plt.plot(x_vals, y_vals2, label="Second Order ODE Solution")
    
    plt.xlabel("t / x")
    plt.ylabel("y(t) / y(x)")
    plt.legend()
    plt.show()

plot_sympy_solution()