python
maks_forsøk = 3
forsøk = 0

while True:
    brukernavn = input("Brukernavn: ")
    passord = input("Passord: ")

    # Kode for å autentisere brukeren

    if autentisert:
        print("Innlogging vellykket!")
        break
    else:
        forsøk += 1
        if forsøk >= maks_forsøk:
            print("For mange mislykkede forsøk. Konto låst.")
            break
        else:
            print("Ugyldig brukernavn eller passord. Prøv igjen.")