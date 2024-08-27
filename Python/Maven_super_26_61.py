python
brukere = {
    "admin": {"passord": "hemmelig", "rolle": "administrator"},
    "bruker1": {"passord": "pass123", "rolle": "bruker"}
}

def autentiser(brukernavn, passord):
    bruker = brukere.get(brukernavn)
    if bruker and bruker["passord"] == passord:
        return bruker["rolle"]
    return None

brukernavn = input("Brukernavn: ")
passord = input("Passord: ")

rolle = autentiser(brukernavn, passord)
if rolle:
    print(f"Innlogging vellykket. Rolle: {rolle}")
    if rolle == "administrator":
        print("Du har administrative rettigheter.")
    elif rolle == "bruker":
        print("Du har brukertillatelser.")
else:
    print("Innlogging mislyktes")