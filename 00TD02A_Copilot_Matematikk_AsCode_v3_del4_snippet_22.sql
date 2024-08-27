-- Enable SSL in my.cnf
[mysqld]
ssl-ca=/path/to/ca-cert.pem
ssl-cert=/path/to/server-cert.pem
ssl-key=/path/to/server-key.pem

-- Create a new user with specific privileges
CREATE USER 'readonly'@'localhost'

 IDENTIFIED BY 'password';
GRANT SELECT ON testdb.* TO 'readonly'@'localhost';