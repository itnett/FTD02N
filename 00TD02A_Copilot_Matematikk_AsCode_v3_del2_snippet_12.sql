-- Eksempel på sammentrekning av uttrykk
SELECT student_id, cpu_usage, memory_usage, 
       cpu_usage / (cpu_usage + memory_usage) AS cpu_ratio 
FROM PerformanceMetrics;