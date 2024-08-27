python
def valider_passord(passord):
    if len(passord) < 8:
        return False
    if not any(c.isupper() for c in passord):
        return False
    if not any(c.islower() for c in passord):
        return False
    if not any(c.isdigit() for c in passord):
        return False
    return True

passord = input("Skriv inn et passord: ")
if valider_passord(passord):
    print("Passordet er gyldig")
else:
    print("Passordet er ugyldig")