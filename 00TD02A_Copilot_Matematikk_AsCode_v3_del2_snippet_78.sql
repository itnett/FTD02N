SELECT student_id, 
       (cpu_usage * 2) + memory_usage AS result 
FROM PerformanceMetrics;