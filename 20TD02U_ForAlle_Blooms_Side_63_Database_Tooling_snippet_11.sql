-- Bruk EXPLAIN og Query Profiler til å feilsøke en SQL-spørring
EXPLAIN SELECT * FROM ordre WHERE kunde_id = 1;

-- Identifiser flaskehalser og optimaliser ved å legge til nødvendige indekser
CREATE INDEX idx_kunde_id ON ordre(kunde_id);