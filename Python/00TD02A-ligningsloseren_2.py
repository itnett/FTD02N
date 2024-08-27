python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Dette programmet løser andregradslikningen ax^2 + bx + c = 0.")
    print("Skriv inn konstantene a, b og c som heltall eller desimaltall.")
    
    # Tar imot koeffisientene fra brukeren
    a = float(input("Skriv inn konstanten a: "))
    b = float(input("Skriv inn konstanten b: "))
    c = float(input("Skriv inn konstanten c: "))

    # Definerer symbolet x
    x = sp.symbols('x')
    
    # Definerer likningen
    eq = sp.Eq(a*x**2 + b*x + c, 0)
    
    # Løser likningen
    løsninger = sp.solve(eq, x)
    
    # Presenter løsningen
    if len(løsninger) == 0:
        print("Likningen har ingen reelle løsninger.")
    elif len(løsninger) == 1:
        print(f"Likningen har én løsning: x = {løsninger[0]}")
    else:
        print(f"Likningen har to løsninger: x1 = {løsninger[0]}, x2 = {løsninger[1]}")
    
    # Plotting
    plot_eq(a, b, c, løsninger)

def plot_eq(a, b, c, løsninger):
    # Definerer symbolet x
    x = sp.symbols('x')
    
    # Lager funksjonen for plotting
    f = a*x**2 + b*x + c
    
    # Konverterer til en funksjon som kan evalueres numerisk
    f_lambdified = sp.lambdify(x, f, 'numpy')
    
    # Genererer x-verdier
    x_vals = np.linspace(-10, 10, 400)
    
    # Beregner y-verdier
    y_vals = f_lambdified(x_vals)
    
    # Lager plottet
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f'{a}x^2 + {b}x + {c}')
    
    # Plotter løsningene
    for løsning in løsninger:
        if sp.im(løsning) == 0:  # Sjekker om løsningen er reell
            plt.plot([løsning.evalf()], [0], 'ro')
            plt.annotate(f'x = {løsning.evalf()}', (løsning.evalf(), 0), textcoords="offset points", xytext=(0,10), ha='center')
    
    # Legger til detaljer i plottet
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title("Plot av andregradslikningen og dens løsninger")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()