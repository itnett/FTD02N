sql
-- Beregning av CPU-bruk multiplisert med 2 og lagt til minnebruk
SELECT student_id, cpu_usage, memory_usage, 
       (cpu_usage * 2) + memory_usage AS result 
FROM PerformanceMetrics;