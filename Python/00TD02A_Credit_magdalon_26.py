python
def sjekk_passordstyrke(passord):
    styrke = 0
    if any(c.islower() for c in passord):
        styrke += 1
    if any(c.isupper() for c in passord):
        styrke += 1
    if any(c.isdigit() for c in passord):
        styrke += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in passord):
        styrke += 1
    return styrke

passord = input("Skriv inn et passord: ")
styrke = sjekk_passordstyrke(passord)
print(f"Passordstyrke: {styrke}/4")