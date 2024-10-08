python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, diff, lambdify, sin, cos, tan, pi, sqrt, expand, factor, simplify, Matrix
from fractions import Fraction

# ... (Hovedmeny, matematikk_meny, fysikk_meny, studieretning_meny fra forrige svar)

def algebra():
    """
    Presents the algebra submenu and allows the user to select a specific operation.

    Presenterer algebra-undermenyen og lar brukeren velge en spesifikk operasjon.
    """

    while True:
        print("\nAlgebra:")
        print("1. Regneregler")
        print("2. Brøk og prosentregning")
        print("3. Potenser")
        print("4. Tall på standardform")
        print("5. Sammentrekning og faktorisering")
        print("0. Tilbake til hovedmenyen")

        valg = input("Ditt valg: ")

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
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def regneregler():
    """
    Performs basic arithmetic operations (+, -, *, /) on two numbers provided by the user.

    Utfører grunnleggende aritmetiske operasjoner (+, -, *, /) på to tall oppgitt av brukeren.
    """

    try:
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
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

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
            print("Ugyldig valg. Vennligst prøv igjen.")

def addere_broker():
    """
    Adds two fractions provided by the user and displays the result in simplified form.

    Adderer to brøker oppgitt av brukeren og viser resultatet i forenklet form.
    """

    try:
        teller1 = int(input("Skriv inn teller for første brøk: "))
        nevner1 = int(input("Skriv inn nevner for første brøk (ikke 0): "))
        teller2 = int(input("Skriv inn teller for andre brøk: "))
        nevner2 = int(input("Skriv inn nevner for andre brøk (ikke 0): "))

        if nevner1 == 0 or nevner2 == 0:
            raise ValueError("Nevneren kan ikke være 0.")

        resultat = Fraction(teller1, nevner1) + Fraction(teller2, nevner2)
        print(f"Summen av brøkene er: {resultat}")
    except ValueError as e:
        print(f"Ugyldig input: {e}")

# ... (subtrahere_broker, multiplisere_broker, dividere_broker - samme struktur som addere_broker)

def konverter_brok_desimal():
    """
    Converts a fraction provided by the user to a decimal number.

    Konverterer en brøk oppgitt av brukeren til et desimaltall.
    """

    try:
        teller = int(input("Skriv inn teller: "))
        nevner = int(input("Skriv inn nevner (ikke 0): "))

        if nevner == 0:
            raise ValueError("Nevneren kan ikke være 0.")

        desimal = teller / nevner
        print(f"Brøken {teller}/{nevner} er lik desimaltallet {desimal}")
    except ValueError as e:
        print(f"Ugyldig input: {e}")

def beregn_prosent():
    """
    Calculates a percentage of a given number.

    Beregner en prosentandel av et gitt tall.
    """
    
    try:
        heltall = float(input("Skriv inn heltallet: "))
        prosent = float(input("Skriv inn prosentandelen (f.eks. 25 for 25%): "))
        resultat = (prosent / 100) * heltall
        print(f"{prosent}% av {heltall} er: {resultat}")
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def beregn_prosentvis_endring():
    """
    Calculates the percentage increase or decrease between two values.

    Beregner den prosentvise økningen eller reduksjonen mellom to verdier.
    """
    
    try:
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
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def potenser():
    """
    Calculates the result of raising a base number to a given exponent.

    Beregner resultatet av å opphøye et grunntall i en gitt eksponent.
    """

    try:
        base = float(input("Skriv inn grunntallet: "))
        eksponent = float(input("Skriv inn eksponenten: "))
        resultat = base ** eksponent
        print(f"{base} opphøyd i {eksponent} er: {resultat}")
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def tall_pa_standardform():
    """
    Converts a number to scientific notation (standard form).

    Konverterer et tall til vitenskapelig notasjon (standardform).
    """
    
    try:
        tall = float(input("Skriv inn tallet: "))
        standardform = "{:.2e}".format(tall)  # Formaterer til to desimaler
        print(f"Tallet {tall} på standardform er: {standardform}")
    except ValueError:
        print("U