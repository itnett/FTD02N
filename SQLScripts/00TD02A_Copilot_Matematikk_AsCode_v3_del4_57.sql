sql
-- Beregning med potenser
SELECT 
    server_name, 
    POWER(network_traffic, 2) AS squared_traffic 
FROM ServerPerformance;