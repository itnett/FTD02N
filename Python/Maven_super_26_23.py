python
def divisjon(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError:
        return "Kan ikke dele med null!"
    except TypeError:
        return "Ugyldige datatyper!"
    else:
        return resultat
    finally:
        print("Forsøkte å dele tall.")

print(divisjon(10, 2))  # Utskrift: 5.0
print(divisjon(10, 0))  # Utskrift: Kan ikke dele med null!
print(divisjon(10, "a"))  # Utskrift:

 Ugyldige datatyper!