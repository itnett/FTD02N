python
def is_valid_username(username):
    return username.isalnum() and 3 <= len(username) <= 20

brukernavn = input("Skriv inn brukernavn: ")
if is_valid_username(brukernavn):
    print("Gyldig brukernavn")
else:
    print("Ugyldig brukernavn")