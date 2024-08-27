bash
#!/bin/bash

# Generer RSA nøkkelpar
openssl genpkey -algorithm RSA -out private_key.pem
openssl rsa -pubout -in private_key.pem -out public_key.pem

# Krypter en melding
echo "This is a secret message." > message.txt
openssl rsautl -encrypt -inkey public_key.pem -pubin -in message.txt -out encrypted_message.bin

# Dekrypter meldingen
openssl rsautl -decrypt -inkey private_key.pem -in encrypted_message.bin -out decrypted_message.txt

echo "Decrypted Message:"
cat decrypted_message.txt