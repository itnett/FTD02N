# Eksempel på implementering av TLS/SSL for kryptering av data under transport i MySQL
# Opprette sertifikat og nøkkel
openssl req -newkey rsa:2048 -days 365 -nodes -keyout mysql-server.key -out mysql-server.crt -x509

# Konfigurer MySQL for å bruke SSL
mysql_ssl_rsa_setup --datadir=/var/lib/mysql

# Oppdatere MySQL-konfigurasjon
[mysqld]
ssl-ca=/var/lib/mysql/ca.pem
ssl-cert=/var/lib/mysql/server-cert.pem
ssl-key=/var/lib/mysql/server-key.pem

# Restart MySQL for å aktivere SSL
systemctl restart mysql