sql
-- Eksempel på en indeksert spørring for optimalisering
CREATE INDEX idx_lønn ON ansatte(lønn);

SELECT * FROM ansatte WHERE lønn > 50000;