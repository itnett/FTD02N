sql
-- Create the table
CREATE TABLE PerformanceMetrics (
    student_id UUID PRIMARY KEY,
    cpu_usage float,
    memory_usage float,
    network_traffic float,
    disk_usage float,
    network_latency float
);

-- Insert data
INSERT INTO PerformanceMetrics (student_id, cpu_usage, memory_usage, network_traffic, disk_usage, network_latency)
VALUES (uuid(), 75.5, 60.2, 500.0, 250.0, 20.5);

-- Query to calculate percentage utilization
SELECT student_id, cpu_usage, memory_usage, 
       ((cpu_usage + memory_usage) / 2) * 100 AS percentage_utilization 
FROM PerformanceMetrics;