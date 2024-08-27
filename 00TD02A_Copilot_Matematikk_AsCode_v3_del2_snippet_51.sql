SELECT student_id, 
       (cpu_usage + memory_usage) / 2 AS avg_utilization 
FROM PerformanceMetrics;