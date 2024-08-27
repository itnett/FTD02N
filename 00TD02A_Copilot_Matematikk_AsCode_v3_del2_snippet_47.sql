SELECT student_id, network_traffic, 
       FORMAT(network_traffic, 'E') AS network_traffic_standard_form 
FROM PerformanceMetrics;