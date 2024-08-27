sql
-- Beregning av hypotenusen i en rettvinklet trekant
SELECT 
    a, b, 
    SQRT(POW(a, 2) + POW(b, 2)) AS hypotenuse 
FROM RightTriangles;