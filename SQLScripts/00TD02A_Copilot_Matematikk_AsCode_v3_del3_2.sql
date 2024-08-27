sql
-- Create the table
CREATE TABLE PerformanceMetrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    cpu_usage REAL,
    memory_usage REAL,
    network_traffic REAL,
    disk_usage REAL,
    network_latency REAL
);

-- Insert data
INSERT INTO PerformanceMetrics (student_id, cpu_usage, memory_usage, network_traffic, disk_usage, network_latency)
VALUES (1, 75.5, 60.2, 500.0, 250.0, 20.5);

-- Query to calculate percentage utilization
SELECT student_id, 
       ((cpu_usage + memory_usage) / 2) * 100 AS percentage_utilization 
FROM PerformanceMetrics;