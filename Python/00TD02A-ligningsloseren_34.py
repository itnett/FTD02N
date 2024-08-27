python
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def input_ligninger():
    antall_ligninger = int(input("Skriv inn antall ligninger i systemet: "))
    variabler = input("Skriv inn variablene (skilt med mellomrom): ").split()
    ligninger = []

    for i in range(antall_ligninger):
        ligning = input(f"Skriv inn ligning {i + 1}: ")
        ligninger.append(sp.sympify(ligning))

    return ligninger, variabler

def solve_and_plot_linear(ligninger, variabler):
    løsninger = sp.linsolve(ligninger, variabler)
    løsninger = list(løsninger)
    
    if not løsninger:
        print("Ingen løsninger for ligningssettet.")
        return
    
    løsning = løsninger[0]
    løsning_dict = dict(zip(variabler, løsning))
    
    print("Løsningene er:")
    for var in variabler:
        print(f"{var} = {løsning_dict[sp.Symbol(var)]}")
    
    if len(variabler) == 2:
        x = sp.Symbol(variabler[0])
        y_løsninger = [sp.solve(ligning, variabler[1])[0] for ligning in ligninger]

        x_vals = np.linspace(-10, 10, 400)
        plt.figure(figsize=(8, 6))

        for y_løsning in y_løsninger:
            y_func = sp.lambdify(x, y_løsning, 'numpy')
            y_vals = y_func(x_vals)
            plt.plot(x_vals, y_vals, label=str(y_løsning))

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.legend()
        plt.show()

def solve_and_plot_nonlinear(ligninger, variabler):
    løsninger = sp.nonlinsolve(ligninger, variabler)
    løsninger = list(løsninger)
    
    if not løsninger:
        print("Ingen løsninger for ligningssettet.")
        return
    
    print("Løsningene er:")
    for løsning in løsninger:
        løsning_dict = dict(zip(variabler, løsning))
        for var in variabler:
            print(f"{var} = {løsning_dict[sp.Symbol(var)]}")
    
    if len(variabler) == 2:
        x, y = sp.symbols(variabler)
        y_løsninger = [sp.solve(ligning, y)[0] for ligning in ligninger]

        x_vals = np.linspace(-10, 10, 400)
        plt.figure(figsize=(8, 6))

        for y_løsning in y_løsninger:
            y_func = sp.lambdify(x, y_løsning, 'numpy')
            y_vals = y_func(x_vals)
            plt.plot(x_vals, y_vals, label=str(y_løsning))

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.legend()
        plt.show()

def main():
    print("Velkommen! Dette programmet løser ligningssett.")
    ligninger, variabler = input_ligninger()
    
    if all([ligning.is_linear for ligning in ligninger]):
        print("Løser lineært ligningssett...")
        solve_and_plot_linear(ligninger, variabler)
    else:
        print("Løser ikke-lineært ligningssett...")
        solve_and_plot_nonlinear(ligninger, variabler)

if __name__ == "__main__":
    main()