python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, diff, lambdify, sin, cos, tan, pi, sqrt, expand, factor, simplify, Matrix
from sklearn.linear_model import LinearRegression
from math import radians, factorial, gcd, comb
from fractions import Fraction

# Importer moduler for hvert emne (disse vil vi lage senere)
import algebra_modul
import trigonometri_geometri_modul
import funksjoner_modul
import fysikk_modul
import studieretning_modul

def main():
    """Main function to display the main menu and guide the user through the learning platform."""

    while True:
        print("\nVelkommen til Fysikk- og Matematikklæreren!")
        print("Velg emne:")
        print("1. Matematikk")
        print("2. Fysikk")
        print("3. Studieretningsspesifikke temaer")
        print("0. Avslutt")

        valg = input("Ditt valg: ")

        if valg == '1':
            algebra_modul.algebra_meny()  # Kaller menyen fra algebra_modul
        elif valg == '2':
            fysikk_modul.fysikk_meny()  # Kaller menyen fra fysikk_modul
        elif valg == '3':
            studieretning_modul.studieretning_meny()  # Kaller menyen fra studieretning_modul
        elif valg == '0':
            print("Avslutter programmet. Takk for at du brukte Fysikk- og Matematikklæreren!")
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

if __name__ == "__main__":
    main()