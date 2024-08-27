sql
SELECT student_id, cpu_usage, memory_usage,
       CASE 
           WHEN cpu_usage > 70 AND memory_usage > 70 THEN 'High Usage'
           ELSE 'Normal Usage'
       END AS usage_status
FROM PerformanceMetrics;