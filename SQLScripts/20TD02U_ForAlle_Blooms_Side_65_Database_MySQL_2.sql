sql
-- Krypter en kolonne med sensitive data
CREATE TABLE kunder (
    kunde_id INT PRIMARY KEY,
    navn VARCHAR(50),
    personnummer VARBINARY(255)
);

-- Sett inn krypterte data
INSERT INTO kunder (kunde_id, navn, personnummer)
VALUES (1, 'Ola Nordmann', AES_ENCRYPT('12345678901', 'hemmelig_nøkkel'));

-- Hent og dekrypter data
SELECT navn, AES_DECRYPT(personnummer, 'hemmelig_nøkkel') AS personnummer FROM kunder;