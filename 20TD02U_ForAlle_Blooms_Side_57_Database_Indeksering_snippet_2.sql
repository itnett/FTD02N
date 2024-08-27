-- Sett inn mange rader i tabellen for testing
INSERT INTO elever (id, navn, alder)
VALUES (1, 'Ola Nordmann', 16),
       (2, 'Kari Nordmann', 17),
       ...
       (1000000, 'Per Hansen', 18);

-- Mål ytelsen til en spørring før og etter opprettelse av indeks
EXPLAIN SELECT * FROM elever WHERE navn = 'Kari Nordmann';