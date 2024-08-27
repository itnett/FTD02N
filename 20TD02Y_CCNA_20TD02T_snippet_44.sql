CREATE USER 'readonly'@'localhost' IDENTIFIED BY 'readonlypassword';
   GRANT SELECT ON studentdb.* TO 'readonly'@'localhost';
   FLUSH PRIVILEGES;

   CREATE USER 'admin'@'localhost' IDENTIFIED BY 'adminpassword';
   GRANT ALL PRIVILEGES ON studentdb.* TO 'admin'@'localhost';
   FLUSH PRIVILEGES;