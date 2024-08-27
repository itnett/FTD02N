bash
echo "Hello, World!" > message.txt
openssl dgst -sha256 -sign private_key.pem -out signature.bin message.txt