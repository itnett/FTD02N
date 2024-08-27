python
import random
from Crypto.Util import number

# Generer store primtall
p = number.getPrime(8)
q = number.getPrime(8)

# Beregn n og phi_n
n = p * q
phi_n = (p - 1) * (q - 1)

# Velg en offentlig eksponent
e = 65537

# Beregn den private eksponenten
d = pow(e, -1, phi_n)

# Meldingen vi vil kryptere
message = 42

# Kryptering
ciphertext = pow(message, e, n)
print("Ciphertext:", ciphertext)

# Dekryptering
decrypted_message = pow(ciphertext, d, n)
print("Decrypted message:", decrypted_message)