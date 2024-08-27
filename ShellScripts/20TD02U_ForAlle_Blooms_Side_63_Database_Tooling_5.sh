bash
# Benchmarking med sysbench for å evaluere MySQL-ytelsen
sysbench --test=oltp --oltp-table-size=1000000 --mysql-db=testdb --mysql-user=root --mysql-password=secret prepare
sysbench --test=oltp --oltp-table-size=1000000 --mysql-db=testdb --mysql-user=root --mysql-password=secret run

# Sammenlign resultatene med en lignende test i PostgreSQL ved hjelp av pgbench
pgbench -i -s 100 testdb
pgbench -c 10 -j 2 -t 10000 testdb