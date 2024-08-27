sql
-- Opprett en tabell for klasser
CREATE TABLE klasser (
    klasse_id INT PRIMARY KEY,
    klasse_navn VARCHAR(10)
);

-- Oppdater eleven-tabellen for å inkludere en fremmednøkkel
CREATE TABLE elever (
    elev_id INT PRIMARY KEY,
    navn VARCHAR(100),
    alder INT,
    klasse_id INT,
    FOREIGN KEY (klasse_id) REFERENCES klasser(klasse_id)
);

-- Sett inn data i begge tabellene
INSERT INTO klasser (klasse_id, klasse_navn) VALUES (1, '10A');
INSERT INTO elever (elev_id, navn, alder, klasse_id) VALUES (1, 'Ola Nordmann', 15, 1);