-- Boolsk algebra: Finn servere med høy utnyttelse og lav latenstid
SELECT 
    server_name 
FROM ServerPerformance 
WHERE cpu_usage > 80 AND network_latency < 50;