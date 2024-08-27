-- Beregning av gjennomsnitt og standardavvik
SELECT AVG(value) AS mean_value, 
       STDDEV(value) AS std_dev 
FROM Statistics;