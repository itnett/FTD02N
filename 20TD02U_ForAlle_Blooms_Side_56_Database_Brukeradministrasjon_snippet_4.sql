-- Aktivere generell spørringslogg i MySQL for overvåking
SET GLOBAL general_log = 'ON';
SET GLOBAL general_log_file = '/var/log/mysql/general.log';

-- Se innholdet i loggfilen
SHOW VARIABLES LIKE 'general_log_file';