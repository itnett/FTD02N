sql
SELECT (c1*b2 - c2*b1) / (a1*b2 - a2*b1) AS x,
       (a1*c2 - a2*c1) / (a1*b2 - a2*b1) AS y
FROM LinearEquations;