-- Bruk av regresjon (lineær) for å predikere fremtidig CPU-bruk
-- Forutsatt SQL-funksjoner for regresjon
SELECT server_name, 
       REGEXP_SUBSTR(regr_slope(cpu_usage, recorded_at), '-?[0-9]+.[0-9]+') AS slope,
       REGEXP_SUBSTR(regr_intercept(cpu_usage, recorded_at), '-?[0-9]+.[0-9]+') AS intercept
FROM ServerPerformance
GROUP BY server_name;