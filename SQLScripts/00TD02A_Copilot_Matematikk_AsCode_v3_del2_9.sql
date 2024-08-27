sql
-- Beregning av eksponentiell vekst i nettverkstrafikk over 5 år med 5% årlig vekst
SELECT student_id, network_traffic, 
       network_traffic * POWER(1.05, 5) AS projected_traffic_5_years 
FROM PerformanceMetrics;