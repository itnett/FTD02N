python
def autentiser(brukernavn, passord):
    # Dette er et forenklet eksempel. I praksis bør du bruke sikre metoder og hash passord.
    if brukernavn == "admin" and passord == "hemmelig":
        return True
    return False

brukernavn = input("Brukernavn: ")
passord = input("Passord: ")

if autentiser(brukernavn, passord):
    print("Innlogging vellykket")
else:
    print("Innlogging mislyktes")