-- Beregning av volum og overflateareal av en kube
SELECT 
    length, 
    POW(length, 3) AS volume, 
    6 * POW(length, 2) AS surface_area 
FROM Cubes;