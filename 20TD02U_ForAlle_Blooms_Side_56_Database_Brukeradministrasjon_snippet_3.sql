-- Opprette en gruppe i MySQL
CREATE USER 'developer'@'localhost' IDENTIFIED BY 'devpassword';

-- Gi utviklergruppen rettigheter til å kjøre SELECT, INSERT og UPDATE
GRANT SELECT, INSERT, UPDATE ON skole.* TO 'developer'@'localhost';

-- Opprette en bruker og tilordne dem til utviklergruppen
GRANT developer TO 'john_doe'@'localhost';