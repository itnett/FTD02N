sql
-- Enable logging in my.cnf
general_log = 1
general_log_file = /var/log/mysql/mysql.log

-- Restart MariaDB service
sudo systemctl restart mariadb