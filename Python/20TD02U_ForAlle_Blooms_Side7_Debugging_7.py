python
def del_tall(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError:
        print("Feil: Kan ikke dele på null!")
        resultat = None
    finally:
        print("Ferdig med divisjon.")
    return resultat

print(del_tall(10, 2))  # Utdata: 5.0
print(del_tall(10, 0))  # Utdata: Feil: Kan ikke dele på null!