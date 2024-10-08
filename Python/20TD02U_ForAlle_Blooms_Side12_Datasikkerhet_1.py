python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Generer et nøkkelpar
privat_nøkkel = rsa.generate_private_key(public_exponent=65537, key_size=2048)
offentlig_nøkkel = privat_nøkkel.public_key()

# Krypter en melding med offentlig nøkkel
melding = b"Dette er veldig hemmelig"
kryptert_melding = offentlig_nøkkel.encrypt(
    melding,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Dekrypter meldingen med privat nøkkel
dekryptert_melding = privat_nøkkel.decrypt(
    kryptert_melding,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(dekryptert_melding)