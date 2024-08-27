-- Sammentrekning av uttrykk
SELECT 
    server_name, 
    (cpu_usage + memory_usage) / total_usage AS usage_ratio 
FROM ServerPerformance;