sql
-- Eksempel på avansert logging-konfigurasjon i PostgreSQL
-- Aktivere logging av langsomme spørringer (spørringer som tar mer enn 500 ms)
SET log_min_duration_statement = 500;

-- Aktivere logging av alle feil, advarsler, og brukertilgang
SET log_statement = 'all';
SET log_connections = 'on';
SET log_disconnections = 'on';