bash
openssl ecparam -genkey -name secp256k1 -out private_key.pem
openssl ec -in private_key.pem -pubout -out public_key.pem