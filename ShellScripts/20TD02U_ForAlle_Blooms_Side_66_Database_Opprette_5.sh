bash
# Installer sysbench (for Ubuntu/Debian)
sudo apt-get install sysbench

# Forbered database for test
sysbench --db-driver=mysql --mysql-user=root --mysql-password=passord123 --mysql-db=benchmark_db oltp_read_write prepare

# Utfør en ytelsestest
sysbench --db-driver=mysql --mysql-user=root --mysql-password=passord123 --mysql-db=benchmark_db oltp_read_write run

# Rydd opp etter test
sysbench --db-driver=mysql --mysql-user=root --mysql-password=passord123 --mysql-db=benchmark_db oltp_read_write cleanup