SELECT student_id
FROM PerformanceMetrics
WHERE (cpu_usage + memory_usage) / 2 > 80;