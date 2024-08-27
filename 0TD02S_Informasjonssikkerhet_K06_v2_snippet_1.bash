# Generer et privat nøkkelpar
openssl genpkey -algorithm RSA -out private_key.pem

# Ekstraher den offentlige nøkkelen
openssl rsa -in private_key.pem -pubout -out public_key.pem