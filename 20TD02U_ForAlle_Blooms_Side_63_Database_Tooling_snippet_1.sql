-- Opprett en enkel tabell med en primærnøkkel
CREATE TABLE kunder (
    kunde_id INT PRIMARY KEY,
    navn VARCHAR(100),
    adresse VARCHAR(255)
);

-- Sett inn noen data
INSERT INTO kunder (kunde_id, navn, adresse) VALUES (1, 'Ola Nordmann', 'Oslo');