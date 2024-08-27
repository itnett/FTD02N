sql
-- Enable SSL in postgresql.conf
ssl = on

-- Reload configuration
SELECT pg_reload_conf();