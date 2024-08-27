sql
-- Beregning av energiforbruk (forenklet eksempel)
SELECT server_name,
       cpu_usage * power_consumption_per_cpu AS power_usage -- Effektforbruk (watt)
FROM ServerPerformance
JOIN ServerSpecs ON ServerPerformance.server_name = ServerSpecs.server_name;