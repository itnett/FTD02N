-- Opprette en ny bruker i MySQL
CREATE USER 'student'@'localhost' IDENTIFIED BY 'securepassword';

-- Gi den nye brukeren tilgang til en spesifikk database
GRANT ALL PRIVILEGES ON skole.* TO 'student'@'localhost';