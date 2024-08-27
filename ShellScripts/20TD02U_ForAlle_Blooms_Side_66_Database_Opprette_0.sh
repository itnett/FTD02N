bash
# Logg inn på MySQL-serveren
mysql -u root -p

# Opprett en database
CREATE DATABASE skole;

# Bruk databasen
USE skole;

# Opprett en tabell
CREATE TABLE elever (
    elev_id INT PRIMARY KEY,
    navn VARCHAR(100),
    klasse VARCHAR(10)
);

# Sett inn data i tabellen
INSERT INTO elever (elev_id, navn, klasse) VALUES (1, 'Ola Nordmann', '10A');

# Sjekk innholdet i tabellen
SELECT * FROM elever;