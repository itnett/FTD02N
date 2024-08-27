-- Bruk DBeaver til å kjøre en avansert SQL-spørring
SELECT kunder.navn, ordre.dato, produkter.navn AS produktnavn
FROM kunder
JOIN ordre ON kunder.kunde_id = ordre.kunde_id
JOIN ordrelinjer ON ordre.ordre_id = ordrelinjer.ordre_id
JOIN produkter ON ordrelinjer.produkt_id = produkter.produkt_id
WHERE ordre.dato BETWEEN '2023-01-01' AND '2023-12-31';