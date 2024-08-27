-- Select all records
SELECT * FROM PerformanceMetrics;

-- Select specific columns
SELECT student_id, cpu_usage, memory_usage FROM PerformanceMetrics;

-- Where clause
SELECT * FROM PerformanceMetrics WHERE cpu_usage > 70;

-- Aggregate functions
SELECT AVG(cpu_usage) AS avg_cpu_usage, MAX(memory_usage) AS max_memory_usage FROM PerformanceMetrics;