sql
-- Beregning av arbeid
SELECT force, distance, 
       force * distance AS work_done 
FROM WorkCalculations;