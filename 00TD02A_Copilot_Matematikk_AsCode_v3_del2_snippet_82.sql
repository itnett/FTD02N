SELECT student_id, 
       cpu_usage / (cpu_usage + memory_usage) AS cpu_ratio 
FROM PerformanceMetrics;