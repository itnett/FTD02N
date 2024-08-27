-- Omforming av et uttrykk for beregning av gjennomsnitt
SELECT server_name, 
       (cpu_usage + memory_usage) / 2 AS avg_utilization 
FROM ServerPerformance;