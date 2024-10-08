python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, diff, lambdify, sin, cos, tan, pi, sqrt, expand, factor, simplify, Matrix
from sklearn.linear_model import LinearRegression
from math import radians

# ... (tidligere kode for algebra, trigonometri og geometri, funksjoner, innledende fysikk)

def kraft_og_rettlinjet_bevegelse():
    # ... (kode for Newtons lover)

def bevegelseslikninger_konstant_fart():
    # ... (kode for bevegelseslikninger med konstant fart)

def bevegelseslikninger_konstant_akselerasjon():
    """
    Calculates distance, time, initial velocity, final velocity, or acceleration for motion with constant acceleration.

    Beregner avstand, tid, startfart, sluttfart eller akselerasjon for bevegelse med konstant akselerasjon.
    """

    try:
        print("\nBevegelseslikninger (konstant akselerasjon):")
        print("1. Beregn avstand (s = v0t + 1/2at^2)")
        print("2. Beregn tid (t = (v - v0) / a)")
        print("3. Beregn startfart (v0 = v - at)")
        print("4. Beregn sluttfart (v = v0 + at)")
        print("5. Beregn akselerasjon (a = (v - v0) / t)")

        valg = input("Skriv inn ditt valg (1-5): ")

        if valg == '1':
            v0 = float(input("Skriv inn startfarten (m/s): "))
            t = float(input("Skriv inn tiden (s): "))
            a = float(input("Skriv inn akselerasjonen (m/s^2): "))
            s = v0 * t + 0.5 * a * t**2
            print(f"Avstanden er: {s:.2f} m")
        elif valg == '2':
            v = float(input("Skriv inn sluttfarten (m/s): "))
            v0 = float(input("Skriv inn startfarten (m/s): "))
            a = float(input("Skriv inn akselerasjonen (m/s^2): "))
            if a == 0:
                print("Akselerasjonen kan ikke være 0.")
            else:
                t = (v - v0) / a
                print(f"Tiden er: {t:.2f} s")
        elif valg == '3':
            v = float(input("Skriv inn sluttfarten (m/s): "))
            a = float(input("Skriv inn akselerasjonen (m/s^2): "))
            t = float(input("Skriv inn tiden (s): "))
            v0 = v - a * t
            print(f"Startfarten er: {v0:.2f} m/s")
        elif valg == '4':
            v0 = float(input("Skriv inn startfarten (m/s): "))
            a = float(input("Skriv inn akselerasjonen (m/s^2): "))
            t = float(input("Skriv inn tiden (s): "))
            v = v0 + a * t
            print(f"Sluttfarten er: {v:.2f} m/s")
        elif valg == '5':
            v = float(input("Skriv inn sluttfarten (m/s): "))
            v0 = float(input("Skriv inn startfarten (m/s): "))
            t = float(input("Skriv inn tiden (s): "))
            if t == 0:
                print("Tiden kan ikke være 0.")
            else:
                a = (v - v0) / t
                print(f"Akselerasjonen er: {a:.2f} m/s^2")
        else:
            print("Ugyldig valg.")
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def energi():
    # ... (kode for energi)

def beregn_arbeid():
    # ... (kode for å beregne arbeid)

def beregn_effekt():
    # ... (kode for å beregne effekt)

def beregn_virkningsgrad():
    # ... (kode for å beregne virkningsgrad)

def beregn_kinetisk_energi():
    """
    Calculates kinetic energy (KE = 1/2mv^2) based on user input.

    Beregner kinetisk energi (KE = 1/2mv^2) basert på brukerinput.
    """

    try:
        masse = float(input("Skriv inn massen (kg): "))
        hastighet = float(input("Skriv inn hastigheten (m/s): "))
        kinetisk_energi = 0.5 * masse * hastighet**2
        print(f"Kinetisk energi er: {kinetisk_energi:.2f} J")
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def beregn_potensiell_energi():
    """
    Calculates gravitational potential energy (PE = mgh) based on user input.

    Beregner potensiell energi (PE = mgh) basert på brukerinput.
    """

    try:
        masse = float(input("Skriv inn massen (kg): "))
        hoyde = float(input("Skriv inn høyden (m): "))
        tyngdeakselerasjon = float(input("Skriv inn tyngdeakselerasjonen (m/s^2, standardverdi 9.81): ") or 9.81)
        potensiell_energi = masse * tyngdeakselerasjon * hoyde
        print(f"Potensiell energi er: {potensiell_energi:.2f} J")
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def anvend_energibevaring():
    """
    Explains the principle of conservation of energy and provides examples.

    Forklarer prinsippet om energibevaring og gir eksempler.
    """

    print("\nEnergibevaring:")
    print("Energi kan ikke skapes eller ødelegges, bare omformes fra én form til en annen.")

    # ... (Legg til eksempler og oppgaver for å illustrere energibevaring)

# Termodynamikkens første lov
def termodynamikkens_forste_lov():
    """
    Explains the first law of thermodynamics (ΔU = Q - W) and performs calculations based on user input.

    Forklarer termodynamikkens første lov (ΔU = Q - W) og utfører beregninger basert på brukerinput.
    """

    print("\nTermodynamikkens første lov:")
    print("Endringen i indre energi (ΔU) til et system er lik varmen tilført systemet (Q) minus arbeidet utført av systemet (W).")

    try:
        q = float(input("Skriv inn varmen tilført systemet (J): "))
        w = float(input("Skriv inn arbeidet utført av systemet (J): "))
        delta_u = q - w
        print(f"Endringen i indre energi er: {delta_u:.2f} J")
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

# ... (Resten av funksjonene for fysikk, termodynamikk og studieretningsspesifikke temaer)

if __name__ == "__main__":
    main()