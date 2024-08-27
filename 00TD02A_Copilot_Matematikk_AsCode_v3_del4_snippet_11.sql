-- Enable logging in postgresql.conf
log_statement = 'all'

-- Reload configuration
SELECT pg_reload_conf();