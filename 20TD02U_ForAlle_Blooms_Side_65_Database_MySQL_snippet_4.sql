-- Aktiver generell logging og slow query logging for sikkerhetsovervåking
SET GLOBAL general_log = 'ON';
SET GLOBAL log_output = 'TABLE';

-- Sjekk general_log for mistenkelig aktivitet
SELECT * FROM mysql.general_log WHERE user_host LIKE 'begrenset_bruker%';