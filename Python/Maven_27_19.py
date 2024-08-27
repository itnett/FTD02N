python
    try:
        number = int(input("Skriv inn et tall: "))
        result = 10 / number
    except ValueError:
        print("Ugyldig input, skriv inn et tall.")
    except ZeroDivisionError:
        print("Kan ikke dele på null.")
    else:
        print(f"Resultatet er: {result}")