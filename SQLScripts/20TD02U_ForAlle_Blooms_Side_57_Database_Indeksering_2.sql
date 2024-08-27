sql
-- Opprette en komposittindeks på 'navn' og 'alder' kolonnene
CREATE INDEX idx_navn_alder ON elever (navn, alder);

-- Bruke komposittindeksen til å akselerere en kompleks spørring
EXPLAIN SELECT * FROM elever WHERE navn = 'Kari Nordmann' AND alder = 17;