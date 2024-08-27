sql
-- Eksempel på løsning av et system med to ukjente
CREATE TEMPORARY TABLE coefficients (
    a1 INT, b1 INT, c1 INT, a2 INT, b2 INT, c2 INT
);

INSERT INTO coefficients VALUES (2, 3, 5, 4, -1, 3);

SELECT 
    (c1*b2 - c2*b1) / (a1*b2 - a2*b1) AS x,
    (a1*c2 - a2*c1) / (a1*b2 - a2*b1) AS y
FROM coefficients;

DROP TEMPORARY TABLE coefficients;