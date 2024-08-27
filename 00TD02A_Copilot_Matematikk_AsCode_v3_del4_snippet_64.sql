-- Eksempel på løsning av et system med to ukjente
WITH coefficients AS (
    SELECT 
        2 AS a1, 3 AS b1, 5 AS c1, 
        4 AS a2, -1 AS b2, 3 AS c2
)
SELECT 
    (c1*b2 - c2*b1) / (a1*b2 - a2*b1) AS x,
    (a1*c2 - a2*c1) / (a1*b2 - a2*b1) AS y
FROM coefficients;