python
def get_positive_integer():
    while True:
        try:
            tall = int(input("Skriv inn et positivt heltall: "))
            if tall > 0:
                return tall
            else:
                print("Tallet må være positivt.")
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et heltall.")

alder = get_positive_integer()
print(f"Du er {alder} år gammel.")