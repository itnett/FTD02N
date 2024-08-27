sql
-- Aktivere feillogging i MySQL
SET GLOBAL log_error = '/var/log/mysql/error.log';

-- Aktivere binær logg (transaksjonslogg)
SET GLOBAL log_bin = '/var/log/mysql/mysql-bin.log';

-- Se innholdet i feilloggen
SHOW VARIABLES LIKE 'log_error';