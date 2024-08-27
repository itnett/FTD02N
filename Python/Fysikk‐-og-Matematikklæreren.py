python
def pythagoras():
    """
    Calculates the hypotenuse or a leg of a right triangle using the Pythagorean theorem (a² + b² = c²).

    Beregner hypotenusen eller en katet i en rettvinklet trekant ved hjelp av Pytagoras' setning (a² + b² = c²).
    """

    print("Pythagoras' setning:")
    print("I en rettvinklet trekant er kvadratet av hypotenusen lik summen av kvadratene av katetene.")

    while True:
        print("\nHva vil du beregne?")
        print("1. Hypotenusen (c)")
        print("2. En katet (a eller b)")
        print("0. Tilbake")

        valg = input("Ditt valg: ")

        if valg == '1':
            a = float(input("Skriv inn lengden av katet a: "))
            b = float(input("Skriv inn lengden av katet b: "))
            c = sqrt(a**2 + b**2)
            print(f"Hypotenusen (c) er: {c:.2f}")
        elif valg == '2':
            c = float(input("Skriv inn lengden av hypotenusen (c): "))
            annen_katet = float(input("Skriv inn lengden av den andre kateten (a eller b): "))
            katet = sqrt(c**2 - annen_katet**2)
            print(f"Den ukjente kateten er: {katet:.2f}")
        elif valg == '0':
            break
        else:
            print("Ugyldig valg.")