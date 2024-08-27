sql
-- Eksempel på kolonne-kryptering i MySQL
CREATE TABLE brukere (
    id INT PRIMARY KEY,
    navn VARCHAR(50),
    personnummer VARBINARY(255)
);

-- Kryptere data ved innsats
INSERT INTO brukere (id, navn, personnummer)
VALUES (1, 'Ola Nordmann', AES_ENCRYPT('12345678901', 'hemmelignøkkel'));

-- Dekryptere data ved henting
SELECT id, navn, AES_DECRYPT(personnummer, 'hemmelignøkkel') AS personnummer
FROM brukere;