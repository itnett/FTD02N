# Sjekke SSL-sertifikat informasjon for domenet
openssl s_client -connect example.com:443

# Hente detaljer fra SSL-sertifikatet
openssl x509 -in cert.pem -noout -text