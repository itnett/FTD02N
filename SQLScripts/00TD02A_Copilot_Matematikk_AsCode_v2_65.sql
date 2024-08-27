sql
-- Beregning av sinus, cosinus og tangens for en vinkel
SELECT angle, 
       SIN(angle) AS sine, 
       COS(angle) AS cosine, 
       TAN(angle) AS tangent 
FROM Angles;