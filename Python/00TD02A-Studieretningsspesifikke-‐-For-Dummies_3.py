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
    x = 1000  # Standard verdi
    log_x = math.log10(x)  # Beregner base 10 logaritmen til x
    print(f"Logaritmen til {x} i base 10 er: {log_x}")

    x_vals = np.linspace(1, 1000, 400)
    y_vals = np.log10(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals, label="y = log10(x)")
    plt.xlabel("x")
    plt.ylabel("log10(x)")
    plt.title("Grafen til logaritmefunksjonen log10(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

def kombinatorikk():
    """
    Denne funksjonen utforsker permutasjoner og kombinasjoner.
    """
    n = 5  # Antall objekter
    k = 3  # Antall valg

    permutasjoner = math.factorial(n)
    print(f"Antall permutasjoner av {n} objekter er: {permutasjoner}")

    kombinasjoner = math.comb(n, k)
    print(f"Antall kombinasjoner av {n} objekter valgt {k} om gangen er: {kombinasjoner}")

def sannsynlighet_og_statistikk():
    """
    Denne funksjonen beregner grunnleggende sannsynligheter og statistikk.
    """
    gunstige_ess = 4
    totale_kort = 52
    sannsynlighet_ess = gunstige_ess / totale_kort
    print(f"Sannsynligheten for å trekke et ess fra en kortstokk er: {sannsynlighet_ess:.2f}")

    data = [3, 7, 7, 2, 9]
    gjennomsnitt = np.mean(data)
    median = np.median(data)
    print(f"Gjennomsnittet av datasettet {data} er: {gjennomsnitt:.2f}")
    print(f"Medianen av datasettet {data} er: {median:.2f}")

    plt.figure()
    plt.hist(data, bins=range(1, 11), alpha=0.7, edgecolor='black')
    plt.xlabel("Verdi")
    plt.ylabel("Frekvens")
    plt.title("Histogram av datasettet")
    plt.grid(True)
    plt.show()

def faser_og_faseoverganger():
    """
    Denne funksjonen forklarer faser og faseoverganger.
    """
    print("Vann kan være i følgende faser: fast (is), flytende (vann), gass (damp).")
    print("Faseoverganger inkluderer smelting, fordamping, kondensasjon, frysing, sublimering og deponering.")

def varme_og_indre_energi():
    """
    Denne funksjonen forklarer varme og indre energi, samt beregner endringen i indre energi.
    """
    masse = 1.0  # kg
    spesifikk_varmekapasitet = 4184  # J/(kg*C), for vann
    temperaturendring = 10.0  # C
    varme = masse * spesifikk_varmekapasitet * temperaturendring
    print(f"Varme som kreves for å øke temperaturen på 1 kg vann med 10°C er: {varme} J")

def termofysikkens_2_hovedsetning():
    """
    Denne funksjonen forklarer termofysikkens andre hovedsetning.
    """
    print("Termofysikkens 2. hovedsetning sier at entropien i et isolert system aldri minker.")
    print("Varme flyter spontant fra varme til kalde områder, ikke omvendt.")

def varmekapasitet_og_kalorimetri():
    """
    Denne funksjonen forklarer varmekapasitet og kalorimetri, samt utfører en beregning.
    """
    masse = 0.1  # kg
    spesifikk_varmekapasitet = 385  # J/(kg*C), for kobber
    temperaturendring = 5.0  # C
    varme = masse * spesifikk_varmekapasitet * temperaturendring
    print(f"Varme som kreves for å øke temperaturen på 100 g kobber med 5°C er: {varme} J")

def tallsystemer():
    """
    Denne funksjonen forklarer binære, desimale og heksadesimale tallsystemer og konverterer mellom dem.
    """
    binær = "1101"
    desimal = int(binær, 2)
    heksadesimal = hex(desimal)
    print(f"Binær: {binær} => Desimal: {desimal} => Heksadesimal: {heksadesimal}")

def algoritmisk_tenking():
    """
    Denne funksjonen forklarer algoritmisk tenking, boolsk algebra og enkle algoritmer.
    """
    a = True
    b = False
    print(f"Boolsk algebra: {a} AND {b} = {a and b}")
    print(f"Boolsk algebra: {a} OR {b} = {a or b}")
    print(f"Boolsk algebra: NOT {a} = {not a}")

    data = [3, 7, 2, 9, 5]
    største = max(data)
    print(f"Største tallet i listen {data} er: {største}")

def main():
    """
    Hovedfunksjonen som viser en meny og lar brukeren velge hvilke operasjoner som skal utføres.
    """
    while True:
        print("\nVelg en operasjon:")
        print("1. Briggske logaritmer")
        print("2. Kombinatorikk")
        print("3. Sannsynlighetsregning og statistikk")
        print("4. Faser og faseoverganger")
        print("5. Varme og indre energi")
        print("6. Termofysikkens 2. hovedsetning")
        print("7. Varmekapasitet og kalorimetri")
        print("8. Tallsystemer")
        print("9. Algoritmisk tenking")
        print("0. Avslutt")

        valg = input("Skriv inn ditt valg (0-9): ")

        if valg == "1":
            briggske_logaritmer()
        elif valg == "2":
            kombinatorikk()
        elif valg == "3":
            sannsynlighet_og_statistikk()
        elif valg == "4":
            faser_og_faseoverganger()
        elif valg == "5":
            varme_og_indre_energi()
        elif valg == "6":
            termofysikkens_2_hovedsetning()
        elif valg == "7":
            varmekapasitet_og_kalorimetri()
        elif valg == "8":
            tallsystemer()
        elif valg == "9":
            algoritmisk_tenking()
        elif valg == "0":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg, vennligst prøv igjen.")

if __name__ == "__main__":
    main()