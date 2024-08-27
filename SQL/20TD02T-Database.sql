sql
-- Hente alle kunder
SELECT * FROM kunder;

-- Legge til en ny kunde
INSERT INTO kunder (navn, epost) VALUES ('Ola Nordmann', 'ola.nordmann@eksempel.no');

-- Oppdatere en kundes e-postadresse
UPDATE kunder SET epost = 'ola.nordmann@nyttdomene.no' WHERE kunde_id = 1;

-- Slette en kunde
DELETE FROM kunder WHERE kunde_id = 1;