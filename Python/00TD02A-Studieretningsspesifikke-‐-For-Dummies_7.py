python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, diff, lambdify, sin, cos, tan, pi, sqrt, expand, factor, simplify, Matrix
from sklearn.linear_model import LinearRegression

# Matematikk
def algebra():
    while True:
        print("\nAlgebra:")
        print("1. Regneregler")
        print("2. Brøk og prosentregning")
        print("3. Potenser")
        print("4. Tall på standardform")
        print("5. Sammentrekning og faktorisering")
        print("6. Likninger av første grad")
        print("7. Likninger av andre grad")
        print("8. Likningssett med to ukjente")
        print("0. Tilbake til hovedmenyen")

        valg = input("Skriv inn ditt valg (0-8): ")

        if valg == '1':
            regneregler()
        elif valg == '2':
            brok_og_prosentregning()
        elif valg == '3':
            potenser()
        elif valg == '4':
            tall_pa_standardform()
        elif valg == '5':
            sammentrekning_og_faktorisering()
        elif valg == '6':
            los_forstegradslikning()
        elif valg == '7':
            los_andregradslikning()
        elif valg == '8':
            los_likningssett()
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def regneregler():
    num1 = float(input("Skriv inn det første tallet: "))
    num2 = float(input("Skriv inn det andre tallet: "))
    operator = input("Skriv inn operatoren (+, -, *, /): ")

    if operator == '+':
        resultat = num1 + num2
    elif operator == '-':
        resultat = num1 - num2
    elif operator == '*':
        resultat = num1 * num2
    elif operator == '/':
        if num2 != 0:
            resultat = num1 / num2
        else:
            print("Kan ikke dele med null.")
            return
    else:
        print("Ugyldig operator.")
        return

    print(f"{num1} {operator} {num2} = {resultat}")

def brok_og_prosentregning():
    while True:
        print("\nBrøk og prosentregning:")
        print("1. Addisjon av brøker")
        print("2. Subtraksjon av brøker")
        print("3. Multiplikasjon av brøker")
        print("4. Divisjon av brøker")
        print("5. Konvertering mellom brøk og desimaltall")
        print("6. Beregning av prosent")
        print("7. Beregning av prosentvis økning/reduksjon")
        print("0. Tilbake til algebra-menyen")

        valg = input("Skriv inn ditt valg (0-7): ")

        if valg == '1':
            addere_broker()
        elif valg == '2':
            subtrahere_broker()
        elif valg == '3':
            multiplisere_broker()
        elif valg == '4':
            dividere_broker()
        elif valg == '5':
            konverter_brok_desimal()
        elif valg == '6':
            beregn_prosent()
        elif valg == '7':
            beregn_prosentvis_endring()
        elif valg == '0':
            break
        else:
            print("Ugyldig valg, vennligst prøv igjen.")

def addere_broker():
    teller1 = int(input("Skriv inn teller for første brøk: "))
    nevner1 = int(input("Skriv inn nevner for første brøk (ikke 0): "))
    teller2 = int(input("Skriv inn teller for andre brøk: "))
    nevner2 = int(input("Skriv inn nevner for andre brøk (ikke 0): "))

    if nevner1 == 0 or nevner2 == 0:
        print("Ugyldig input. Nevneren kan ikke være 0.")
        return

    fellesnevner = np.lcm(nevner1, nevner2)
    ny_teller1 = teller1 * (fellesnevner // nevner1)
    ny_teller2 = teller2 * (fellesnevner // nevner2)

    sum_teller = ny_teller1 + ny_teller2
    gcd = math.gcd(sum_teller, fellesnevner)
    if gcd > 1:
        sum_teller //= gcd
        fellesnevner //= gcd

    print(f"Summen av brøkene er: {sum_teller}/{fellesnevner}")

def subtrahere_broker():
    teller1 = int(input("Skriv inn teller for første brøk: "))
    nevner1 = int(input("Skriv inn nevner for første brøk (ikke 0): "))
    teller2 = int(input("Skriv inn teller for andre brøk: "))
    nevner2 = int(input("Skriv inn nevner for andre brøk (ikke 0): "))

    if nevner1 == 0 or nevner2 == 0:
        print("Ugyldig input. Nevneren kan ikke være 0.")
        return

    fellesnevner = np.lcm(nevner1, nevner2)
    ny_teller1 = teller1 * (fellesnevner // nevner1)
    ny_teller2 = teller2 * (fellesnevner // nevner2)

    differanse_teller = ny_teller1 - ny_teller2
    gcd = math.gcd(differanse_teller, fellesnevner)
    if gcd > 1:
        differanse_teller //= gcd
        fellesnevner //= gcd

    print(f"Differansen av brøkene er: {differanse_teller}/{fellesnevner}")

def multiplisere_broker():
    teller1 = int(input("Skriv inn teller for første brøk: "))
    nevner1 = int(input("Skriv inn nevner for første brøk (ikke 0): "))
    teller2 = int(input("Skriv inn teller for andre brøk: "))
    nevner2 = int(input("Skriv inn nevner for andre brøk (ikke 0): "))

    if nevner1 == 0 or nevner2 == 0:
        print("Ugyldig input. Nevneren kan ikke være 0.")
        return

    produkt_teller = teller1 * teller2
    produkt_nevner = nevner1 * nevner2

    gcd = math.gcd(produkt_teller, produkt_nevner)
    if gcd > 1:
        produkt_teller //= gcd
        produkt_nevner //= gcd

    print(f"Produktet av brøkene er: {produkt_teller}/{produkt_nevner}")

def dividere_broker():
    teller1 = int(input("Skriv inn teller for første brøk: "))
    nevner1 = int(input("Skriv inn nevner for første brøk (ikke 0): "))
    teller2 = int(input("Skriv inn teller for andre brøk (ikke 0): "))
    nevner2 = int(input("Skriv inn nevner for andre brøk (ikke 0): "))

    if nevner1 == 0 or nevner2 == 0 or teller2 == 0:
        print("Ugyldig input. Nevneren eller teller2 kan ikke være 0.")
        return

    kvotient_teller = teller1 * nevner2
    kvotient_nevner = nevner1 * teller2

    gcd = math.gcd(kvotient_teller, kvotient_nevner)
    if gcd > 1:
        kvotient_teller //= gcd
        kvotient_nevner //= gcd

    print(f"Kvotienten av brøkene er: {kvotient_teller}/{kvotient_nevner}")

def konverter_brok_desimal():
    teller = int(input("Skriv inn teller: "))
    nevner = int(input("Skriv inn nevner (ikke 0): "))
    if nevner == 0:
        print("Ugyldig input. Nevneren kan ikke være 0.")
        return
    desimal = teller / nevner
    print(f"Brøken {teller}/{nevner} er lik desimaltallet {desimal}")

def beregn_prosent():
    heltall = float(input("Skriv inn heltallet: "))
    prosent = float(input("Skriv inn prosentandelen (f.eks. 25 for 25%): "))
    resultat = (prosent / 100) * heltall
    print(f"{prosent}% av {heltall} er: {resultat}")

def beregn_prosentvis_endring():
    opprinnelig_verdi = float(input("Skriv inn opprinnelig verdi: "))
    ny_verdi = float(input("Skriv inn ny verdi: "))
    endring = ny_verdi - opprinnelig_verdi
    prosentvis_endring = (endring / opprinnelig_verdi) * 100
    if prosentvis_endring > 0:
        print(f"Det er en økning på {prosentvis_endring:.2f}%")
    elif prosentvis_endring < 0:
        print(f"Det er en reduksjon på {-prosentvis_endring:.2f}%")
    else:
        print("Ingen endring")

def potenser():
    base = float(input("Skriv inn grunntallet: "))
    eksponent = float(input("Skriv inn eksponenten: "))
    resultat = base ** eksponent
    print(f"{base} opphøyd i {eksponent} er: {resultat}")

def tall_pa_standardform():
    tall = float(input("Skriv inn tallet: "))
    standardform = "{:.2e}".format(tall)
    print(f"Tallet {tall} på standardform er: {standardform}")

def sammentrekning_og_faktorisering():
    while True:
        print("\nSammentrekning og faktorisering:")
        print("1. Sammentrekning")
        print("2. Faktorisering")
        print("0. Tilbake til algebra-menyen")

        valg = input("Skriv inn ditt valg (0-2): ")

        if valg == '1':
            uttrykk = input("Skriv inn uttrykket du vil sammentrekke: ")
            try:
                forenklet = simplify(uttrykk)
                print(f"Det forenklede uttrykket er: {forenklet}")
            except:
                print("Ugyldig uttrykk. Vennligst prøv igjen.")
        elif valg == '2':
            uttrykk = input("Skriv inn uttrykket du vil faktorisere: ")
            try:
                faktorisert = factor(uttrykk)
                print(f"Det faktoriserte uttrykket er: {faktorisert}")
            except:
                print("Ugyldig uttrykk eller kan ikke faktoriseres. Vennligst prøv igjen.")
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def los_forstegradslikning():
    try:
        a = float(input("Skriv inn koeffisienten a: "))
        b = float(input("Skriv inn koeffisienten b: "))
        x = symbols('x')
        likning = Eq(a*x + b, 0)
        losning = solve(likning, x)

        print(f"Løsningen for likningen {a}x + {b} = 0 er: x = {losning[0]}")

        # Visualisering
        x_vals = np.linspace(-10, 10, 400)
        y_vals = a*x_vals + b
        plt.plot(x_vals, y_vals, label=f'y = {a}x + {b}')
        plt.axhline(0, color='red', linestyle='--', label='y = 0')
        plt.axvline(losning[0], color='green', linestyle='--', label=f'x = {losning[0]}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Likning av Første Grad: {a}x + {b} = 0')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def los_andregradslikning():
    try:
        a = float(input("Skriv inn koeffisienten a: "))
        b = float(input("Skriv inn koeffisienten b: "))
        c = float(input("Skriv inn koeffisienten c: "))
        x = symbols('x')
        likning = Eq(a*x**2 + b*x + c, 0)
        losninger = solve(likning, x)

        if len(losninger) == 0:
            print("Likningen har ingen reelle løsninger.")
        elif len(losninger) == 1:
            print(f"Likningen har én løsning: x = {losninger[0]}")
        else:
            print(f"Likningen har to løsninger: x = {losninger[0]} og x = {losninger[1]}")

        # Visualisering
        x_vals = np.linspace(-10, 10, 400)
        y_vals = a*x_vals**2 + b*x_vals + c
        plt.plot(x_vals, y_vals, label=f'y = {a}x^2 + {b}x + {c}')
        plt.axhline(0, color='red', linestyle='--', label='y = 0')
        for losning in losninger:
            plt.axvline(losning, color='green', linestyle='--', label=f'x = {losning}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Likning av Andre Grad: {a}x^2 + {b}x + {c} = 0')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def los_likningssett():
    try:
        a1 = float(input("Skriv inn koeffisienten a1: "))
        b1 = float(input("Skriv inn koeffisienten b1: "))
        c1 = float(input("Skriv inn konstanten c1: "))
        a2 = float(input("Skriv inn koeffisienten a2: "))
        b2 = float(input("Skriv inn koeffisienten b2: "))
        c2 = float(input("Skriv inn konstanten c2: "))

        x, y = symbols('x y')
        likning1 = Eq(a1*x + b1*y, c1)
        likning2 = Eq(a2*x + b2*y, c2)

        losning = solve((likning1, likning2), (x, y))

        if losning:
            print(f"Løsningen for likningssettet er: x = {losning[x]}, y = {losning[y]}")

            # Visualisering
            x_vals = np.linspace(-10, 10, 400)
            y_vals1 = (c1 - a1*x_vals) / b1
            y_vals2 = (c2 - a2*x_vals) / b2

            plt.plot(x_vals, y_vals1, label=f'{a1}x + {b1}y = {c1}')
            plt.plot(x_vals, y_vals2, label=f'{a2}x + {b2}y = {c2}')
            plt.scatter(losning[x], losning[y], color='red', label='Løsning')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Likningssett')
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print("Likningssettet har ingen eller uendelig mange løsninger.")
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")
def omforme_formler():
    formel_str = input("Skriv inn formelen du vil omforme (f.eks. 'y = 3*x + 2'): ")
    variabel_str = input("Hvilken variabel vil du isolere? ")

    try:
        formel = Eq(eval(formel_str.replace("=", ","), {"x": symbols('x'), "y": symbols('y')}))
        losning = solve(formel, symbols(variabel_str))
        if losning:
            print(f"Isolert {variabel_str}: {losning[0]}")
        else:
            print(f"Kunne ikke isolere {variabel_str} i formelen.")
    except:
        print("Ugyldig formel eller variabel. Vennligst prøv igjen.")

# ... (rest av funksjonene for likningsløsning og likningssett)

def trigonometri_og_geometri():
    while True:
        print("\nTrigonometri og geometri:")
        print("1. Beregn areal av ulike figurer")
        print("2. Beregn omkrets av ulike figurer")
        print("3. Beregn volum av ulike figurer")
        print("4. Beregn overflate av ulike figurer")
        print("5. Pytagoras' setning")
        print("6. Trigonometri i rettvinklede trekanter")
        print("7. Vektorer i planet")
        print("0. Tilbake til hovedmenyen")

        valg = input("Skriv inn ditt valg (0-7): ")

        if valg == '1':
            beregn_areal()
        elif valg == '2':
            beregn_omkrets()
        # ... (Implementer de resterende valgene for trigonometri og geometri)
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def beregn_areal():
    while True:
        print("\nVelg figur:")
        print("1. Trekant")
        print("2. Sirkel")
        print("3. Rektangel")
        print("0. Tilbake til trigonometri og geometri-menyen")

        valg = input("Skriv inn ditt valg (0-3): ")

        if valg == '1':
            grunnlinje = float(input("Skriv inn grunnlinjen til trekanten: "))
            hoyde = float(input("Skriv inn høyden til trekanten: "))
            areal = 0.5 * grunnlinje * hoyde
            print(f"Arealet av trekanten er: {areal}")
        elif valg == '2':
            radius = float(input("Skriv inn radius til sirkelen: "))
            areal = pi * radius**2
            print(f"Arealet av sirkelen er: {areal}")
        # ... (Implementer de resterende valgene for arealberegning)
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def beregn_omkrets():
    # ... (Implementer beregning av omkrets for ulike figurer)
    pass

# ... (Resten av funksjonene for trigonometri og geometri, funksjoner, fysikkemner, etc.)

def main():
    # ... (Hovedfunksjonen er den samme som før)

if __name__ == "__main__":
    main()