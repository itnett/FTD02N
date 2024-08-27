-- Eksempel på sammentrekning av uttrykk
SELECT server_name, 
       cpu_usage / (cpu_usage + memory_usage) AS cpu_ratio 
FROM ServerPerformance;