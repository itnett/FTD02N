-- Beregning av energiforbruk
SELECT server_name,
       cpu_usage * power_consumption_per_cpu AS power_usage 
FROM ServerPerformance
JOIN ServerSpecs ON ServerPerformance.server_name = ServerSpecs.server_name;