-- Beregning av serverutnyttelse i prosent
SELECT server_name, 
       (cpu_usage + memory_usage) / 2 AS combined_utilization, -- Gjennomsnittlig utnyttelse
       combined_utilization * 100 AS percentage_utilization -- Prosentvis utnyttelse
FROM ServerPerformance;