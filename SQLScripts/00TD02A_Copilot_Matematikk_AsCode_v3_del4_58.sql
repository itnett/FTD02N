sql
-- Beregning med potenser
SELECT 
    server_name, 
    POW(network_traffic, 2) AS squared_traffic 
FROM ServerPerformance;