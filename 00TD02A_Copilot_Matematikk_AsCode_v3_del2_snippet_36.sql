-- Beregning av kombinasjoner
SELECT n, k, 
       FACT(n) / (FACT(k) * FACT(n - k)) AS combinations 
FROM Combin

atorics;