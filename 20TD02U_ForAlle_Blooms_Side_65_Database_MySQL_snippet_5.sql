-- Kombiner flere sikkerhetstiltak
-- 1. Bruk SSL for å sikre tilkoblinger
ALTER USER 'begrenset_bruker'@'localhost' REQUIRE SSL;

-- 2. Krypter sensitive kolonner
ALTER TABLE kunder ADD COLUMN telefon VARBINARY(255);
UPDATE kunder SET telefon = AES_ENCRYPT('98765432', 'hemmelig_nøkkel') WHERE kunde_id = 1;

-- 3. Aktiver og overvåk logging
SET GLOBAL general_log = 'ON';