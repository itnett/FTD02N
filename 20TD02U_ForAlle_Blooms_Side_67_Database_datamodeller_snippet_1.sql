-- Opprett en enkel tabell med en primærnøkkel
CREATE TABLE elever (
    elev_id INT PRIMARY KEY,
    navn VARCHAR(100),
    alder INT
);

-- Sett inn data i tabellen
INSERT INTO elever (elev_id, navn, alder) VALUES (1, 'Ola Nordmann', 15);