sql
-- Bruk av regresjon (lineær) for å predikere fremtidig CPU-bruk
-- (Krever utvidelser i MySQL eller bruk av statistiske verktøy)
SELECT server_name, 
       REGEXP_SUBSTR(regr_slope(cpu_usage, recorded_at), '-?[0-9]+.[0-9]+') AS slope,
       REGEXP_SUBSTR(regr_intercept(cpu_usage, recorded_at), '-?[0-9]+.[0-9]+') AS intercept
FROM ServerPerformance
GROUP BY server_name;