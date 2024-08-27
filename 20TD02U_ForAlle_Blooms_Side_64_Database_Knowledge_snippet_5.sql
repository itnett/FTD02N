-- Eksempel på opprettelse av en trigger for automatisert behandling
CREATE TRIGGER oppdater_lager
AFTER INSERT ON ordrelinjer
FOR EACH ROW
BEGIN
    UPDATE produkter SET lager = lager - NEW.antall WHERE produkt_id = NEW.produkt_id;
END;