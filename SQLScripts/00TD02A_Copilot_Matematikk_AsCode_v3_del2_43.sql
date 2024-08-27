sql
SELECT student_id, cpu_usage, memory_usage, 
       (cpu_usage * 2) + memory_usage AS result 
FROM PerformanceMetrics;