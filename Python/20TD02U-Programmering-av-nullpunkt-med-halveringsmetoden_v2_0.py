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
    plt.plot(root, f(root), 'ro', label=f'Root ≈ {root:.4f}')
    
    for i, m in enumerate(midpoints):
        plt.plot([a, b], [f(a), f(b)], 'g:')
        plt.plot([m, m], [0, f(m)], 'b:')
        plt.text(m, f(m) + 0.1, f'm{i+1}', ha='center')
    
    plt.title('Bisection Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Input from user
a = float(input("Skriv inn nedre grense i dette intervallet: "))
b = float(input("Skriv inn øvre grense i dette intervallet: "))
tol = float(input("Skriv inn ønsket nøyaktighet (f.eks. 0.0001): "))

try:
    root, midpoints = bisection_method(f, a, b, tol)
    print(f"Nullpunktet er x ≈ {root:.4f}")
    plot_function_and_root(f, a, b, root, midpoints)
except ValueError as e:
    print(e)

Her er hele artikkelen optimalisert for markdown som en kodeblokk: