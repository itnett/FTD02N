sql
SELECT student_id, cpu_usage, memory_usage, 
       (cpu_usage + memory_usage) / 2 AS combined_utilization, 
       ((cpu_usage + memory_usage) / 2) * 100 AS percentage_utilization 
FROM PerformanceMetrics;