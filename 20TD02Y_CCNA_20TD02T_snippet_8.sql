CREATE USER 'student'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON studentdb.* TO 'student'@'localhost';
   FLUSH PRIVILEGES;