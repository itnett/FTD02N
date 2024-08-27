-- Finn studenter der kombinert utnyttelse overstiger en gitt terskel
SELECT student_id
FROM PerformanceMetrics
WHERE (cpu_usage + memory_usage) / 2 > 80;