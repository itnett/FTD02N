python
# Importere nødvendige biblioteker
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Funksjon for å løse en førstegradslikning
def los_forste_gradslikning():
    # Definerer variabelen
    x = symbols('x')
    
    # Likning av første grad: 2x + 3 = 7
    likning = Eq(2*x + 3, 7)
    
    # Løser likningen
    losning = solve(likning, x)
    
    # Gir tilbakemelding på løsningen
    print(f"Løsningen for likningen 2x + 3 = 7 er: x = {losning[0]}")
    
    # Visualiserer likningen
    x_vals = np.linspace(-10, 10, 400)
    y_vals = 2*x_vals + 3
    plt.plot(x_vals, y_vals, label='y = 2x + 3')
    plt.axhline(7, color='red', linestyle='--', label='y = 7')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Likning av Første Grad: 2x + 3 = 7')
    plt.legend()
    plt.grid(True)
    plt.show()

# Funksjon for å løse en andregradslikning
def los_andre_gradslikning():
    # Definerer variabelen
    x = symbols('x')
    
    # Likning av andre grad: x^2 - 5x + 6 = 0
    likning = Eq(x**2 - 5*x + 6, 0)
    
    # Løser likningen
    losninger = solve(likning, x)
    
    # Gir tilbakemelding på løsningene
    print(f"Løsningene for likningen x^2 - 5x + 6 = 0 er: x = {losninger[0]} og x = {losninger[1]}")
    
    # Visualiserer likningen
    x_vals = np.linspace(-10, 10, 400)
    y_vals = x_vals**2 - 5*x_vals + 6
    plt.plot(x_vals, y_vals, label='y = x^2 - 5x + 6')
    plt.axhline(0, color='red', linestyle='--', label='y = 0')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Likning av Andre Grad: x^2 - 5x + 6 = 0')
    plt.legend()
    plt.grid(True)
    plt.show()

# Funksjon for å løse et likningssett med to ukjente
def los_likningssett():
    # Definerer variablene
    x, y = symbols('x y')
    
    # Likningssett: 2x + y = 10 og x - y = 2
    likning1 = Eq(2*x + y, 10)
    likning2 = Eq(x - y, 2)
    
    # Løser likningssettet
    losning = solve((likning1, likning2), (x, y))
    
    # Gir tilbakemelding på løsningen
    print(f"Løsningen for likningssettet er: x = {losning[x]}, y = {losning[y]}")
    
    # Visualiserer likningssettet
    x_vals = np.linspace(-10, 10, 400)
    y_vals1 = 10 - 2*x_vals
    y_vals2 = x_vals - 2
    plt.plot(x_vals, y_vals1, label='2x + y = 10')
    plt.plot(x_vals, y_vals2, label='x - y = 2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Likningssett: 2x + y = 10 og x - y = 2')
    plt.legend()
    plt.grid(True)
    plt.show()

# Funksjon for å tilpasse og omforme formeluttrykk
def omforme_formler():
    # Eksempel 1: Isolere x i formelen y = 3x + 2
    x, y = symbols('x y')
    formel = Eq(y, 3*x + 2)
    isolert_x = solve(formel, x)
    print(f"Isolere x i formelen y = 3x + 2: x = {isolert_x[0]}")
    
    # Eksempel 2: Tilpasse formelen V = lwh for å isolere h
    V, l, w, h = symbols('V l w h')
    formel2 = Eq(V, l*w*h)
    isolert_h = solve(formel2, h)
    print(f"Isolere h i formelen V = lwh: h = {isolert_h[0]}")
    
    # Visualisering av omformet formel
    x_vals = np.linspace(-10, 10, 400)
    y_vals = 3*x_vals + 2
    x_isolert_vals = (y_vals - 2) / 3

    plt.plot(x_vals, y_vals, label='y = 3x + 2')
    plt.plot(x_isolert_vals, y_vals, label='x isolert: x = (y - 2) / 3', linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Tilpasse og Omforme Formeluttrykk')
    plt.legend()
    plt.grid(True)
    plt.show()

# Hovedfunksjon for å kjøre de ulike delene av skriptet
def main():
    while True:
        print("\nVelg en av følgende operasjoner:")
        print("1: Løse Likninger av Første Grad")
        print("2: Løse Likninger av Andre Grad")
        print("3: Løse Likningssett med To Ukjente")
        print("4: Tilpasse og Omforme Formeluttrykk")
        print("5: Avslutt")
        valg = input("Skriv inn tallet for ditt valg (1-5): ")
        
        if valg == "1":
            los_forste_gradslikning()
        elif valg == "2":
            los_andre_gradslikning()
        elif valg == "3":
            los_likningssett()
        elif valg == "4":
            omforme_formler()
        elif valg == "5":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg, vennligst prøv igjen.")

# Kjør hovedfunksjonen
if __name__ == "__main__":
    main()