sql
-- Hent total vekt av kofferter for en person
SELECT SUM(Vekt) AS TotalVekt
FROM Koffert
WHERE PersonID = 1;

-- Beregn promille for en person
SELECT (Alkohol.Mengde * 1000) / (CASE WHEN Person.Kjønn = 'Mann' THEN 0.7 ELSE 0.6 END * Person.Vekt) AS Promille
FROM Alkohol
JOIN Person ON Alkohol.PersonID = Person.PersonID
WHERE Person.Navn = 'Tormod';