bash
# Logg inn på MariaDB-serveren
mysql -u root -p

# Opprett en database
CREATE DATABASE prosjekt;

# Bruk databasen
USE prosjekt;

# Opprett en tabell
CREATE TABLE prosjekter (
    prosjekt_id INT PRIMARY KEY AUTO_INCREMENT,
    tittel VARCHAR(100),
    start_dato DATE
);

# Sett inn data i tabellen
INSERT INTO prosjekter (tittel, start_dato) VALUES ('Nytt Webprosjekt', '2024-01-01');

# Sjekk innholdet i tabellen
SELECT * FROM prosjekter;