sql
SELECT student_id, 
       POWER(network_traffic, 2) AS squared_network_traffic 
FROM PerformanceMetrics;