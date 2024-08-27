-- Bruk EXPLAIN ANALYZE i PostgreSQL for å evaluere spørringsytelsen
EXPLAIN ANALYZE SELECT * FROM lån WHERE retur_dato IS NULL;

-- Identifiser ineffektive spørringer og optimaliser dem ved å justere strukturen eller legge til indekser
CREATE INDEX idx_retur_dato ON lån(retur_dato);