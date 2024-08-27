sql
-- Opprette brukere og administrere tilgangsnivåer
CREATE USER 'student'@'localhost' IDENTIFIED BY 'passord123';
GRANT SELECT, INSERT ON skole.* TO 'student'@'localhost';

-- Kryptering av sensitive data
CREATE TABLE sensitive_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data BLOB NOT NULL,
    encryption_key VARBINARY(32) NOT NULL
);