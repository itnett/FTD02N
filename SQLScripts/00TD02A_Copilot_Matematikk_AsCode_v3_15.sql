sql
-- Konvertering mellom ulike enheter
SELECT quantity_in_meters, 
       quantity_in_meters / 1000 AS quantity_in_kilometers 
FROM Measurements;