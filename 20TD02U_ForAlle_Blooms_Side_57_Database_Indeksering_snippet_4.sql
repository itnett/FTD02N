-- Analyser hvordan indekser brukes i spørringer
EXPLAIN SELECT * FROM elever WHERE alder = 17;

-- Identifiser indekser som kanskje ikke er nødvendige
SHOW INDEX FROM elever;