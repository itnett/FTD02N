sql
-- Bruk EXPLAIN for å analysere en spørring
EXPLAIN SELECT * FROM ordre WHERE kunde_id = 1;

-- Legg til en indeks for å forbedre ytelsen
CREATE INDEX idx_kunde_id ON ordre(kunde_id);