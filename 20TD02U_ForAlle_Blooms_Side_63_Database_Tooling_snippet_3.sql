-- Eksempel på en ACID-transaksjon i MySQL
START TRANSACTION;

-- Utfør en rekke operasjoner
UPDATE kunder SET adresse = 'Bergen' WHERE kunde_id = 1;
INSERT INTO ordre (ordre_id, kunde_id, dato) VALUES (1, 1, CURDATE());

-- Forplikte transaksjonen (COMMIT) eller rulle tilbake (ROLLBACK) ved feil
COMMIT;