python
def del_tall(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError:
        print("Feil: Kan ikke dele på null!")
    else:
        print("Resultatet er:", resultat)
    finally:
        print("Uansett hva som skjer, vil denne linjen alltid kjøres.")