python
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (1/3)*x**3 + (1/2)*x**2 - x - 1

def bisection_method(f, a, b, tol=0.0001):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    midpoints = []
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        midpoints.append(midpoint)
        
        if f(midpoint) == 0:
            return midpoint, midpoints
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    
    return (a + b) / 2, midpoints

def plot_function_and_root(f, a, b, root, midpoints):
    x = np.linspace(a, b, 400)
    y = f(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x) = (1/3)*x^3 + (1/2)*x^2 - x - 1')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.plot(root, f(root), 'ro', label=f'root ≈ {root:.4f}')
    
    for i, m in enumerate(midpoints):
        plt.plot([a, b], [f(a), f(b)], 'g:')
        plt.plot([m, m], [0, f(m)], 'b:')
        plt.text(m, f(m) + 0.1, f'm{i+1}', ha='center')
    
    plt.title('bisection method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def get_valid_input():
    while True:
        try:
            a = float(input("skriv inn nedre grense i dette intervallet: "))
            b = float(input("skriv inn øvre grense i dette intervallet: "))
            if a >= b:
                print("nedre grense må være mindre enn øvre grense. prøv igjen.")
                continue
            tol = float(input("skriv inn ønsket nøyaktighet (f.eks. 0.0001): "))
            if f(a) * f(b) >= 0:
                print("f(a) og f(b) må ha motsatte fortegn. prøv igjen.")
                continue
            return a, b, tol
        except ValueError as e:
            print(f"ugyldig inndata: {e}. prøv igjen.")

# hovedprogram
a, b, tol = get_valid_input()

try:
    root, midpoints = bisection_method(f, a, b, tol)
    print(f"nullpunktet er x ≈ {root:.4f}")
    plot_function_and_root(f, a, b, root, midpoints)
except ValueError as e:
    print(e)