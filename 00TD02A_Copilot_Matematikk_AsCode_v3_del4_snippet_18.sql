-- Enable SSL in my.cnf
[mysqld]
ssl-ca=/path/to/ca-cert.pem
ssl-cert=/path/to/server-cert.pem
ssl-key=/path/to/server-key.pem

-- Restart MariaDB service
sudo systemctl restart mariadb