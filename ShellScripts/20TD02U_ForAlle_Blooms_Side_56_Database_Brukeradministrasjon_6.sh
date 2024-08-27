bash
#!/bin/bash

# Skript for å opprette en bruker med to-faktor autentisering i MySQL
mysql -u root -p -e "
CREATE USER 'secure_user'@'localhost' IDENTIFIED BY 'securepassword';
GRANT SELECT, INSERT ON skole.* TO 'secure_user'@'localhost';
ALTER USER 'secure_user'@'localhost' REQUIRE SSL;
"

# Opprette et sertifikat for SSL-autentisering
openssl req -new -x509 -days 365 -nodes -out /etc/mysql/mysql-cert.pem -keyout /etc/mysql/mysql-key.pem