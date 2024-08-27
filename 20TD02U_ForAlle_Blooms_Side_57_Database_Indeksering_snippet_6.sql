-- Identifiser og fjern overflødige indekser
DROP INDEX idx_navn ON elever;

-- Gjennomfør revisjon av indekser
SHOW INDEX FROM elever;

-- Fjerne ineffektive indekser som ikke brukes
DROP INDEX idx_alder ON elever;