sql
-- Løsning av et system med to ukjente (forenklet eksempel)
-- Anta vi har en tabell som inneholder koeffisienter og konstanter for likninger
CREATE TABLE LinearEquations (
    a1 DECIMAL(5,2),
    b1 DECIMAL(5,2),
    c1 DECIMAL(5,2),
    a2 DECIMAL(5,2),
    b2 DECIMAL(5,2),
    c2 DECIMAL(5,2)
);

-- Sett inn eksempeldata
INSERT INTO LinearEquations VALUES (2, 3, 5, 4, -1, 3);

-- Løs likningssettet a1*x + b1*y = c1 og a2*x + b2*y = c2
SELECT (c1*b2 - c2*b1) / (a1*b2 - a2*b1) AS x,
       (a1*c2 - a2*c1) / (a1*b2 - a2*b1) AS y
FROM LinearEquations;