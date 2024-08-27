bash
# Bruk av MySQL Workbench for å sette opp replikering mellom en lokal database og AWS RDS
# Start replikering for å holde data synkronisert mellom on-premises og cloud
CHANGE MASTER TO MASTER_HOST='rds-endpoint.amazonaws.com',
MASTER_USER='replica_user',
MASTER_PASSWORD='replica_password',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=107;

START SLAVE;