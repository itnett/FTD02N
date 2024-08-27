-- Eksempel på en JOIN-operasjon
SELECT ansatte.navn, ansatte.stilling, avdelinger.avdeling_navn
FROM ansatte
JOIN avdelinger ON ansatte.avdeling_id = avdelinger.avdeling_id;