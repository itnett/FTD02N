sql
-- Create a database for IT operations
CREATE DATABASE IT_Operations;

-- Use the database
USE IT_Operations;

-- Create a table to store server performance data
CREATE TABLE ServerPerformance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    server_name VARCHAR(255),
    cpu_usage DECIMAL(5,2), -- CPU usage as a percentage
    memory_usage DECIMAL(5,2), -- Memory usage as a percentage
    network_traffic DECIMAL(10,2), -- Network traffic in MB
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data into the table
INSERT INTO ServerPerformance (server_name, cpu_usage, memory_usage, network_traffic)
VALUES 
('Server1', 75.5, 60.2, 500.0),
('Server2', 65.0, 55.5, 300.0),
('Server3', 85.3, 70.1, 800.0);

-- Query to calculate average CPU usage across all servers
SELECT AVG(cpu_usage) AS avg_cpu_usage FROM ServerPerformance;

-- Query to identify servers with CPU usage above 80%
SELECT server_name, cpu_usage 
FROM ServerPerformance 
WHERE cpu_usage > 80;

-- Query to predict future network traffic based on current data (simplified linear projection)
SELECT server_name, network_traffic * 1.1 AS projected_network_traffic
FROM ServerPerformance;