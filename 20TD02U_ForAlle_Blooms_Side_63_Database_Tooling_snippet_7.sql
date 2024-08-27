-- Opprett en trigger for å håndtere forretningslogikk automatisk
CREATE TRIGGER oppdater_lager
AFTER INSERT ON ordrelinjer
FOR EACH ROW
BEGIN
    UPDATE produkter SET lager = lager - NEW.antall WHERE produkt_id = NEW.produkt_id;
END;

-- Opprett en lagret prosedyre for å håndtere komplekse transaksjoner
CREATE PROCEDURE behandle_ordre(IN ordreId INT)
BEGIN
    DECLARE total DECIMAL(10, 2);
    SELECT SUM(pris * antall) INTO total FROM ordrelinjer WHERE ordre_id = ordreId;
    INSERT INTO betalinger (ordre_id, beløp, dato) VALUES (ordreId, total, CURDATE());
END;