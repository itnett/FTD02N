-- Create a new user
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

-- Grant privileges
GRANT ALL PRIVILEGES ON testdb.* TO 'newuser'@'localhost';