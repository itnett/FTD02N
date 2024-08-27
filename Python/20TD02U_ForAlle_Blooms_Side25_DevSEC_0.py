python
import re

# Validerer en e-postadresse
def er_gyldig_epost(epost):
    mønster = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(mønster, epost) is not None

epost = input("Skriv inn e-postadresse: ")
if er_gyldig_epost(epost):
    print("Gyldig e-postadresse")
else:
    print("Ugyldig e-postadresse")