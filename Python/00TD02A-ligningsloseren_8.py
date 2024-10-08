python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import deepxde as dde

# 1. Solve Differential Equations using SymPy

def solve_first_order_ode_sympy():
    t = sp.symbols('t')
    y = sp.Function('y')(t)
    ode = sp.Eq(sp.diff(y, t), t * y)
    ySol = sp.dsolve(ode)
    print("SymPy løsning for første ordens differensiallikning:")
    sp.pretty_print(ySol)

    # Initialbetingelse
    cond = sp.Eq(y.subs(t, 0), 2)
    ySol_cond = sp.dsolve(ode, ics={y.subs(t, 0): 2})
    print("SymPy løsning med initialbetingelse y(0) = 2:")
    sp.pretty_print(ySol_cond)

def solve_nonlinear_ode_sympy():
    t = sp.symbols('t')
    y = sp.Function('y')(t)
    ode = sp.Eq((sp.diff(y, t) + y)**2, 1)
    ySol = sp.dsolve(ode)
    print("SymPy løsning for ikke-lineær differensiallikning:")
    sp.pretty_print(ySol)

    # Initialbetingelse
    cond = sp.Eq(y.subs(t, 0), 0)
    ySol_cond = sp.dsolve(ode, ics={y.subs(t, 0): 0})
    print("SymPy løsning med initialbetingelse y(0) = 0:")
    sp.pretty_print(ySol_cond)

def solve_second_order_ode_sympy():
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    Dy = y.diff(x)
    ode = sp.Eq(y.diff(x, 2), sp.cos(2 * x) - y)
    cond1 = sp.Eq(y.subs(x, 0), 1)
    cond2 = sp.Eq(Dy.subs(x, 0), 0)
    ySol = sp.dsolve(ode, ics={y.subs(x, 0): 1, Dy.subs(x, 0): 0})
    ySol = sp.simplify(ySol)
    print("SymPy løsning for andre ordens differensiallikning med initialbetingelser:")
    sp.pretty_print(ySol)

def solve_third_order_ode_sympy():
    x = sp.symbols('x')
    u = sp.Function('u')(x)
    Du = u.diff(x)
    D2u = u.diff(x, 2)
    ode = sp.Eq(u.diff(x, 3), u)
    cond1 = sp.Eq(u.subs(x, 0), 1)
    cond2 = sp.Eq(Du.subs(x, 0), -1)
    cond3 = sp.Eq(D2u.subs(x, 0), sp.pi)
    uSol = sp.dsolve(ode, ics={u.subs(x, 0): 1, Du.subs(x, 0): -1, D2u.subs(x, 0): sp.pi})
    print("SymPy løsning for tredje ordens differensiallikning med initialbetingelser:")
    sp.pretty_print(uSol)

# 2. Solve Differential Equations using DeepXDE (PINNs)

def solve_ode_pinn():
    # Define the ODE system
    def ode_system(t, u):
        du_t = dde.grad.jacobian(u, t)
        return du_t - tf.math.cos(2 * np.pi * t)

    def boundary(t, on_initial):
        return on_initial and np.isclose(t[0], 0)

    # Define geometry and initial condition
    geom = dde.geometry.TimeDomain(0, 2)
    ic = dde.IC(geom, lambda t: 1, boundary)

    # Define problem
    data = dde.data.PDE(geom, ode_system, ic, num_domain=30, num_boundary=2, solution=lambda t: np.sin(2 * np.pi * t) / (2 * np.pi) + 1, num_test=100)

    # Define the neural network
    net = dde.maps.FNN([1] + [32] * 2 + [1], "tanh", "Glorot uniform")
    model = dde.Model(data, net)
    model.compile("adam", lr=0.001)

    # Train the model
    losshistory, train_state = model.train(epochs=6000)
    dde.saveplot(losshistory, train_state, issave=False, isplot=True)

    # Predictions
    test_t = np.linspace(0, 2, 100)
    pred_u = model.predict(test_t).flatten()
    true_u = np.sin(2 * np.pi * test_t) / (2 * np.pi) + 1

    # Plot results
    plt.figure(figsize=(10, 8))
    plt.plot(test_t, true_u, label="True solution")
    plt.plot(test_t, pred_u, '--', label="PINN prediction")
    plt.xlabel("t")
    plt.ylabel("u(t)")
    plt.legend()
    plt.show()

def main():
    print("Løsning av differensiallikninger med SymPy")
    
    # SymPy solutions
    solve_first_order_ode_sympy()
    solve_nonlinear_ode_sympy()
    solve_second_order_ode_sympy()
    solve_third_order_ode_sympy()
    
    print("Løsning av differensiallikninger med PINNs (DeepXDE)")
    
    # PINNs solution
    solve_ode_pinn()

if __name__ == "__main__":
    main()