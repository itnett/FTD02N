python
# ... (tidligere kode for algebra, hovedmeny, undermenyer)

def trigonometri_og_geometri():
    """
    Presents the trigonometry and geometry submenu and allows the user to select a specific operation.

    Presenterer undermenyen for trigonometri og geometri og lar brukeren velge en spesifikk operasjon.
    """

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
        elif valg == '3':
            beregn_volum()
        elif valg == '4':
            beregn_overflate()
        elif valg == '5':
            pythagoras()
        elif valg == '6':
            trigonometri()
        elif valg == '7':
            vektorer()
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def beregn_areal():
    """
    Calculates the area of different geometric shapes based on user input.

    Beregner arealet av forskjellige geometriske figurer basert på brukerinput.
    """

    while True:
        print("\nVelg figur:")
        print("1. Trekant")
        print("2. Sirkel")
        print("3. Rektangel")
        print("4. Parallellogram")
        print("5. Trapes")
        print("0. Tilbake til trigonometri og geometri-menyen")

        valg = input("Skriv inn ditt valg (0-5): ")

        if valg == '1':
            grunnlinje = float(input("Skriv inn grunnlinjen til trekanten: "))
            hoyde = float(input("Skriv inn høyden til trekanten: "))
            areal = 0.5 * grunnlinje * hoyde
            print(f"Arealet av trekanten er: {areal}")
        elif valg == '2':
            radius = float(input("Skriv inn radius til sirkelen: "))
            areal = pi * radius**2
            print(f"Arealet av sirkelen er: {areal}")
        elif valg == '3':
            lengde = float(input("Skriv inn lengden til rektangelet: "))
            bredde = float(input("Skriv inn bredden til rektangelet: "))
            areal = lengde * bredde
            print(f"Arealet av rektangelet er: {areal}")
        elif valg == '4':
            grunnlinje = float(input("Skriv inn grunnlinjen til parallellogrammet: "))
            hoyde = float(input("Skriv inn høyden til parallellogrammet: "))
            areal = grunnlinje * hoyde
            print(f"Arealet av parallellogrammet er: {areal}")
        elif valg == '5':
            a = float(input("Skriv inn lengden av den ene parallelle siden til trapeset: "))
            b = float(input("Skriv inn lengden av den andre parallelle siden til trapeset: "))
            hoyde = float(input("Skriv inn høyden til trapeset: "))
            areal = 0.5 * (a + b) * hoyde
            print(f"Arealet av trapeset er: {areal}")
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def beregn_omkrets():
    """
    Calculates the perimeter of different geometric shapes based on user input.

    Beregner omkretsen av forskjellige geometriske figurer basert på brukerinput.
    """

    while True:
        print("\nVelg figur:")
        print("1. Trekant")
        print("2. Sirkel")
        print("3. Rektangel")
        print("0. Tilbake til trigonometri og geometri-menyen")

        valg = input("Skriv inn ditt valg (0-3): ")

        if valg == '1':
            side1 = float(input("Skriv inn lengden av side 1: "))
            side2 = float(input("Skriv inn lengden av side 2: "))
            side3 = float(input("Skriv inn lengden av side 3: "))
            omkrets = side1 + side2 + side3
            print(f"Omkretsen av trekanten er: {omkrets}")
        elif valg == '2':
            radius = float(input("Skriv inn radius til sirkelen: "))
            omkrets = 2 * pi * radius
            print(f"Omkretsen av sirkelen er: {omkrets}")
        elif valg == '3':
            lengde = float(input("Skriv inn lengden til rektangelet: "))
            bredde = float(input("Skriv inn bredden til rektangelet: "))
            omkrets = 2 * (lengde + bredde)
            print(f"Omkretsen av rektangelet er: {omkrets}")
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

# ... (Implementer beregn_volum(), beregn_overflate(), pythagoras(), trigonometri() og vektorer() på lignende måte)

if __name__ == "__main__":
    main()