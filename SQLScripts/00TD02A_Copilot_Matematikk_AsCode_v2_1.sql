sql
-- Projisering av fremtidig trafikk med eksponentiell vekst
SELECT server_name, 
       network_traffic * POWER(1.05, 5) AS projected_traffic_5_years 
FROM ServerPerformance;