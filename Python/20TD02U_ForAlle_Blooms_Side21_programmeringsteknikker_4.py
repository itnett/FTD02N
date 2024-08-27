python
# Definerer en enkel funksjon uten parametere
def hei():
    print("Hei, verden!")

# Kaller funksjonen
hei()

# Funksjon med parametere
def legg_til(a, b):
    return a + b

# Kaller funksjonen med argumenter
resultat = legg_til(3, 5)
print(resultat)  # Skriver ut 8

# Funksjon med standardparametere
def velkomstmelding(navn="gjest"):
    print(f"Velkommen, {navn}!")

# Kaller funksjonen med og uten argumenter
velkomstmelding("Alice")
velkomstmelding()