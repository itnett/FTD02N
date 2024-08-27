sql
-- Create the class
CREATE CLASS PerformanceMetrics EXTENDS V;

-- Insert data
INSERT INTO PerformanceMetrics SET student_id = 1, cpu_usage = 75.5, memory_usage = 60.2, network_traffic = 500.0, disk_usage = 250.0, network_latency = 20.5;

-- Query to calculate percentage utilization
SELECT student_id, ((cpu_usage + memory_usage) / 2) * 100 AS percentage_utilization FROM PerformanceMetrics;