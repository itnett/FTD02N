python
import random
import string

def generer_passord(lengde=12):
    tegn = string.ascii_letters + string.digits + string.punctuation
    passord = ''.join(random.choice(tegn) for i in range(lengde))
    return passord

passord = generer_passord()
print(passord)