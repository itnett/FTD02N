bash
# Eksempel på å sette opp en Galera Cluster for MySQL
# Start tre MySQL noder som skal delta i clusteren
service mysql start --wsrep-new-cluster
mysql -u root -e "SET GLOBAL wsrep_cluster_address='gcomm://192.168.0.1,192.168.0.2,192.168.0.3';"