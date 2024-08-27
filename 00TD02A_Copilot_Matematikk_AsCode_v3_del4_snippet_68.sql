-- Beregning av hypotenusen i en rettvinklet trekant
SELECT 
    a, b, 
    SQRT(POWER(a, 2) + POWER(b, 2)) AS hypotenuse 
FROM RightTriangles;