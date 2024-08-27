python
def get_brukerinput():
    while True:
        try:
            tall = int(input("Skriv inn et heltall: "))
            return tall
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et heltall.")