-- Beregning av volum og overflateareal av en kube
SELECT 
    length, 
    POWER(length, 3) AS volume, 
    6 * POWER(length, 2) AS surface_area 
FROM Cubes;