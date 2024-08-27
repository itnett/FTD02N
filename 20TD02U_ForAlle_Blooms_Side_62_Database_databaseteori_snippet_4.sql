-- Bruk EXPLAIN for å analysere spørringsytelsen
EXPLAIN SELECT * FROM ordre_ny WHERE produkt_id = 1;

-- Optimaliser ytelsen ved å legge til en indeks
CREATE INDEX idx_produkt_id ON ordre_ny(produkt_id);