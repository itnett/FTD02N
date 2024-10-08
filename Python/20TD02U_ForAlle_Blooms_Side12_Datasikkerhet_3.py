python
import pyotp

# Generer en hemmelig nøkkel
hemmelig_nøkkel = pyotp.random_base32()
totp = pyotp.TOTP(hemmelig_nøkkel)

# Generer en engangskode
engangskode = totp.now()
print(engangskode)

# Verifiser koden (bruker sender denne koden for å logge inn)
print(totp.verify(engangskode))