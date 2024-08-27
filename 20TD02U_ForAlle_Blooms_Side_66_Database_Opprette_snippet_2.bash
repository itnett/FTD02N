# Logg inn på PostgreSQL-serveren
psql -U postgres

# Opprett en database
CREATE DATABASE bedrift;

# Koble til databasen
\c bedrift;

# Opprett en tabell
CREATE TABLE ansatte (
    ansatt_id SERIAL PRIMARY KEY,
    navn VARCHAR(100),
    stilling VARCHAR(50)
);

# Sett inn data i tabellen
INSERT INTO ansatte (navn, stilling) VALUES ('Kari Nordmann', 'Utvikler');

# Sjekk innholdet i tabellen
SELECT * FROM ansatte;