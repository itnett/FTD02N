# Signer en fil med en privat nøkkel
openssl dgst -sha256 -sign private_key.pem -out signature.bin message.txt

# Verifiser signaturen med den offentlige nøkkelen
openssl dgst -sha256 -verify public_key.pem -signature signature.bin message.txt