sql
-- Beregning av serverutnyttelse i prosent
SELECT 
    server_name, 
    (cpu_usage + memory_usage) / 2 AS combined_utilization, 
    ((cpu_usage + memory_usage) / 2) * 100 AS percentage_utilization 
FROM ServerPerformance;