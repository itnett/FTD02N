sql
-- Beregning av massetetthet
SELECT mass, volume, 
       mass / volume AS density 
FROM Materials;