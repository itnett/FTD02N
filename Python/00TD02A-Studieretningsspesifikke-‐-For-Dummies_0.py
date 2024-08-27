python
# Importere nødvendige biblioteker
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
import math

# 1. Briggske Logaritmer
def briggske_logaritmer():
    # Beregn logaritmen av 1000
    x = 1000
    log_x = math.log10(x)
    print(f"Logaritmen til {x} i base 10 er: {log_x}")
    
    # Visualisere logaritmefunksjonen
    x_vals = np.linspace(1, 1000, 400)
    y_vals = np.log10(x_vals)
    plt.plot(x_vals, y_vals, label='y = log10(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Briggske Logaritmer')
    plt.legend()
    plt.grid(True)
    plt.show()

# 2. Kombinatorikk
def kombinatorikk():
    # Beregn antall permutasjoner av 4 objekter
    n = 4
    permutasjoner = math.factorial(n)
    print(f"Antall permutasjoner av {n} objekter er: {permutasjoner}")
    
    # Beregn antall kombinasjoner av 3 objekter valgt fra 5 objekter
    n = 5
    k = 3
    kombinasjoner = math.comb(n, k)
    print(f"Antall kombinasjoner av {k} objekter valgt fra {n} objekter er: {kombinasjoner}")

# 3. Sannsynlighetsregning og Statistikk
def sannsynlighet_og_statistikk():
    # Beregn sannsynligheten for å trekke et ess fra en kortstokk
    gunstige_ess = 4
    totalt_antall_kort = 52
    sannsynlighet_ess = gunstige_ess / totalt_antall_kort
    print(f"Sannsynligheten for å trekke et ess fra en kortstokk er: {sannsynlighet_ess}")

    # Beregn gjennomsnittet og medianen av et datasett
    data = [3, 7, 7, 2, 9]
    gjennomsnitt = np.mean(data)
    median = np.median(data)
    print(f"Gjennomsnittet av datasettet {data} er: {gjennomsnitt}")
    print(f"Medianen av datasettet {data} er: {median}")

# 4. Faser og Faseoverganger
def faser_og_faseoverganger():
    # Forklare faseoverganger med eksempler
    faser = ['Fast', 'Flytende', 'Gass']
    overganger = {
        'Smelting': 'Fast til Flytende',
        'Fordamping': 'Flytende til Gass',
        'Kondensasjon': 'Gass til Flytende',
        'Frysing': 'Flytende til Fast',
        'Sublimasjon': 'Fast til Gass',
        'Deposisjon': 'Gass til Fast'
    }
    print("Faseoverganger:")
    for overgang, beskrivelse i overganger.items():
        print(f"{overgang}: {beskrivelse}")

# 5. Varme og Indre Energi
def varme_og_indre_energi():
    # Beregn varme kreves for å øke temperaturen på 1 kg vann med 10 grader Celsius
    m = 1  # masse i kg
    c = 4.18  # spesifikk varmekapasitet for vann i J/g°C
    delta_T = 10  # temperaturendring i °C
    Q = m * c * delta_T * 1000  # varme i J
    print(f"Varme kreves for å øke temperaturen på 1 kg vann med 10°C er: {Q} J")

# 6. Termofysikkens 2. Hovedsetning
def termofysikk_2_hovedsetning():
    # Forklare termofysikkens 2. hovedsetning
    print("Termofysikkens 2. hovedsetning sier at entropien i et isolert system aldri vil minke. Varme vil spontant flyte fra et varmere til et kaldere objekt.")
    # Eksempel på entropiøkning
    varme_overfort = 500  # J
    temperatur_varmt = 400  # K
    temperatur_kaldt = 300  # K
    delta_S = varme_overfort * (1/temperatur_kaldt - 1/temperatur_varmt)
    print(f"Endring i entropi når {varme_overfort} J varme overføres fra et objekt ved {temperatur_varmt} K til et objekt ved {temperatur_kaldt} K er: {delta_S} J/K")

# 7. Varmekapasitet og Kalorimetri
def varmekapasitet_og_kalorimetri():
    # Beregn spesifikk varmekapasitet
    Q = 500  # J
    m = 100  # g
    delta_T = 10  # °C
    c = Q / (m * delta_T)
    print(f"Den spesifikke varmekapasiteten til stoffet er: {c} J/g°C")

# 8. Tallsystemer
def tallsystemer():
    # Konverter binær til desimal
    binar_tall = "1101"
    desimal_tall = int(binar_tall, 2)
    print(f"{binar_tall} i binær er {desimal_tall} i desimal")

    # Konverter desimal til heksadesimal
    desimal_tall = 47
    heksadesimal_tall = hex(desimal_tall)
    print(f"{desimal_tall} i desimal er {heksadesimal_tall} i heksadesimal")

# 9. Algoritmisk Tenking
def algoritmisk_tenking():
    # Sannhetstabell for A AND B
    A = [True, True, False, False]
    B = [True, False, True, False]
    AND = [a and b for a, b in zip(A, B)]
    print("Sannhetstabell for A AND B:")
    print("A\tB\tA AND B")
    for a, b, ab in zip(A, B, AND):
        print(f"{a}\t{b}\t{ab}")

    # Enkel algoritme for å finne minste tallet i en liste
    def finn_minste_tall(liste):
        minste_tall = liste[0]
        for tall in liste[1:]:
            if tall < minste_tall:
                minste_tall = tall
        return minste_tall

    liste = [3, 7, 1, 9, 4]
    minste_tall = finn_minste_tall(liste)
    print(f"Det minste tallet i listen {liste} er: {minste_tall}")

# Hovedfunksjon for å kjøre de ulike delene av skriptet
def main():
    while True:
        print("\nVelg en av følgende operasjoner:")
        print("1: Briggske Logaritmer")
        print("2: Kombinatorikk")
        print("3: Sannsynlighetsregning og Statistikk")
        print("4: Faser og Faseoverganger")
        print("5: Varme og Indre Energi")
        print("6: Termofysikkens 2. Hovedsetning")
        print("7: Varmekapasitet og Kalorimetri")
        print("8: Tallsystemer")
        print("9: Algoritmisk Tenking")
        print("10: Avslutt")
        valg = input("Skriv inn tallet for ditt valg (1-10): ")
        
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
            termofysikk_2_hovedsetning()
        elif valg == "7":
            varmekapasitet_og_kalorimetri()
        elif valg == "8":
            tallsystemer()
        elif valg == "9":
            algoritmisk_tenking()
        elif valg == "10":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg, vennligst prøv igjen.")

# Kjør hovedfunksjonen
if __name__ == "__main__":
    main()