sql
-- Opprette en bruker med begrenset tilgang i MySQL
CREATE USER 'begrenset_bruker'@'localhost' IDENTIFIED BY 'sterkt_passord';
GRANT SELECT ON skole.* TO 'begrenset_bruker'@'localhost';