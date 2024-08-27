sql
-- Opprett en trigger for å automatisk oppdatere en kolonne ved innsetting i en tabell
CREATE TRIGGER oppdater_låntid
AFTER INSERT ON lån
FOR EACH ROW
BEGIN
    UPDATE bøker SET status = 'Lånt ut' WHERE bok_id = NEW.bok_id;
END;

-- Opprett en lagret prosedyre for å returnere bøker
CREATE PROCEDURE returner_bok(IN bokId INT)
BEGIN
    UPDATE bøker SET status = 'Tilgjengelig' WHERE bok_id = bokId;
    UPDATE lån SET retur_dato = CURDATE() WHERE bok_id = bokId AND retur_dato IS NULL;
END;