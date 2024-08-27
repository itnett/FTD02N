sql
-- Evaluering av logging-konfigurasjonen i PostgreSQL
SHOW log_statement;
SHOW log_connections;
SHOW log_disconnections;

-- Analyser langsomme spørringer for optimalisering
SELECT * FROM pg_stat_activity WHERE state = 'active' AND query_start < NOW() - INTERVAL '500 milliseconds';