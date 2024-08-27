-- Testspørring for å evaluere ytelsen og integriteten til datamodellen
SELECT kunder.navn, produkter.produkt_navn, ordrelinjer.antall, ordrer.ordre_dato
FROM ordrelinjer
JOIN ordrer ON ordrelinjer.ordre_id = ordrer.ordre_id
JOIN kunder ON ordrer.kunde_id = kunder.kunde_id
JOIN produkter ON ordrelinjer.produkt_id = produkter.produkt_id;