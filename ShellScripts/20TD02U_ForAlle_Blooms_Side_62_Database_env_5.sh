bash
# Bruk sysbench til å benchmarke MySQL i forskjellige miljøer
sysbench --test=oltp --oltp-table-size=1000000 --mysql-db=testdb --mysql-user=root --mysql-password=secret prepare
sysbench --test=oltp --oltp-table-size=1000000 --mysql-db=testdb --mysql-user=root --mysql-password=secret run