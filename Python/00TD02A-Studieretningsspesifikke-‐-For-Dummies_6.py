python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math

# Funksjoner som dekker ulike matematiske konsepter
def briggske_logaritmer():
    """
    Denne funksjonen beregner og visualiserer Briggske logaritmer (base 10 logaritmer).
    """
    try:
        x_str = input(f"Skriv inn et positivt tall (standard er 1000): ")
        x = float(x_str) if x_str else 1000
        if x <= 0:
            raise ValueError
    except ValueError:
        print("Ugyldig input. Bruker standardverdi 1000.")
        x = 1000

    log_x = math.log10(x)
    print(f"Logaritmen til {x} i base 10 er: {log_x}")

    x_vals = np.linspace(1, x, 400)  # Juster x-aksen basert på input
    y_vals = np.log10(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals, label="y = log10(x)")
    plt.xlabel("x")
    plt.ylabel("log10(x)")
    plt.title(f"Grafen til logaritmefunksjonen log10(x) opp til x = {x}")  # Oppdater tittel
    plt.legend()
    plt.grid(True)
    plt.show()

def kombinatorikk():
    """
    Denne funksjonen utforsker permutasjoner og kombinasjoner.
    """
    try:
        n_str = input(f"Skriv inn antall objekter (standard er 5): ")
        n = int(n_str) if n_str else 5
        k_str = input(f"Skriv inn antall valg (standard er 3): ")
        k = int(k_str) if k_str else 3
        if n <= 0 or k <= 0 or k > n:
            raise ValueError
    except ValueError:
        print("Ugyldig input. Bruker standardverdier n=5, k=3.")
        n = 5
        k = 3

    permutasjoner = math.factorial(n)
    kombinasjoner = math.comb(n, k)
    print(f"Antall permutasjoner av {n} objekter er: {permutasjoner}")
    print(f"Antall kombinasjoner av {n} objekter valgt {k} om gangen er: {kombinasjoner}")

# ... (Resten av funksjonene med lignende input-prompter)

def main():
    """
    Hovedfunksjonen som viser en meny og lar brukeren velge hvilke operasjoner som skal utføres.
    """
    while True:
        # ... (Meny og valg som før)
        if valg == "1":
            briggske_logaritmer()
        # ... (Resten av valgene som før)

if __name__ == "__main__":
    main()