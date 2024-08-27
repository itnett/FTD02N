python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, diff, lambdify, sin, cos, tan, pi, sqrt, expand, factor, simplify, Matrix
from sklearn.linear_model import LinearRegression

# Matematikk
def algebra():
    # (Koden for algebra er den samme som i forrige svar)

# Trigonometri og geometri
def trigonometri_og_geometri():
    # (Koden for trigonometri og geometri er den samme som i forrige svar)

# Funksjoner
def funksjoner():
    while True:
        print("\nFunksjoner:")
        print("1. Rette linjer")
        print("2. Polynomfunksjoner")
        print("3. Eksponentialfunksjoner")
        print("4. Derivasjon av polynomfunksjoner")
        print("5. Regresjon (lineær)")
        print("0. Tilbake til hovedmenyen")

        valg = input("Skriv inn ditt valg (0-5): ")

        if valg == '1':
            rette_linjer()
        elif valg == '2':
            polynomfunksjoner()
        elif valg == '3':
            eksponentialfunksjoner()
        elif valg == '4':
            derivasjon_av_polynomfunksjoner()
        elif valg == '5':
            regresjon()
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def rette_linjer():
    m = float(input("Skriv inn stigningstallet (m): "))
    b = float(input("Skriv inn konstantleddet (b): "))

    x_values = np.linspace(-10, 10, 100)
    y_values = m * x_values + b

    plt.plot(x_values, y_values, label=f'y = {m}x + {b}')
    plt.title('Graf av en rett linje')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

def polynomfunksjoner():
    # ... (Implementasjon for polynomfunksjoner)

def eksponentialfunksjoner():
    # ... (Implementasjon for eksponentialfunksjoner)

def derivasjon_av_polynomfunksjoner():
    # ... (Implementasjon for derivasjon av polynomfunksjoner)

def regresjon():
    # ... (Implementasjon for lineær regresjon)

# Fysikk
def innledende_fysikk():
    while True:
        print("\nInnledende fysikk:")
        print("1. Anvende SI-systemet og dekadiske prefikser")
        print("2. Begrepene masse, tyngde og massetetthet")
        print("3. Usikkerhet og korrekt bruk av gjeldende siffer")
        print("0. Tilbake til hovedmenyen")

        valg = input("Skriv inn ditt valg (0-3): ")

        if valg == '1':
            si_system_og_prefikser()
        elif valg == '2':
            masse_tyngde_tetthet()
        elif valg == '3':
            usikkerhet_og_gjeldende_siffer()
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def si_system_og_prefikser():
    # ... (Implementasjon for SI-systemet og prefikser)

def masse_tyngde_tetthet():
    # ... (Implementasjon for masse, tyngde og massetetthet)

def usikkerhet_og_gjeldende_siffer():
    # ... (Implementasjon for usikkerhet og gjeldende siffer)

def kraft_og_rettlinjet_bevegelse():
    # ... (Implementasjon for kraft og rettlinjet bevegelse)

def energi():
    # ... (Implementasjon for energi)

# Termodynamikk og studieretningsspesifikke temaer
def termodynamikk_og_studieretning():
    # ... (Implementasjon for termodynamikk og studieretningsspesifikke temaer)

# Hovedmeny
def main():
    while True:
        print("\nVelg et fagområde:")
        print("1. Matematikk")
        print("2. Fysikk")
        print("3. Termodynamikk og studieretning")
        print("0. Avslutt")

        valg = input("Skriv inn ditt valg (0-3): ")

        if valg == '1':
            algebra()
        elif valg == '2':
            innledende_fysikk()
        elif valg == '3':
            termodynamikk_og_studieretning()
        elif valg == '0':
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

if __name__ == "__main__":
    main()