sql
-- Finn servere der kombinert utnyttelse overstiger en gitt terskel (likning)
SELECT server_name
FROM ServerPerformance
WHERE (cpu_usage + memory_usage) / 2 > 80; -- Terskel på 80%