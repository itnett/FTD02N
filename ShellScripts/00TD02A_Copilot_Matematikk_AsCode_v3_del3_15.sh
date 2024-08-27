bash
#!/bin/bash

# Start Docker containers
docker-compose up -d

# Wait for containers to be fully up and running
sleep 20

# PostgreSQL setup
echo "Setting up PostgreSQL..."
docker exec -i $(docker ps -qf "name=postgres") psql -U user -d testdb <<-EOSQL
CREATE TABLE PerformanceMetrics (
    metric_id SERIAL PRIMARY KEY,
    student_id INT,
    cpu_usage FLOAT,
    memory_usage FLOAT,
    network_traffic FLOAT,
    disk_usage FLOAT,
    network_latency FLOAT
);
INSERT INTO PerformanceMetrics (student_id, cpu_usage, memory_usage, network_traffic, disk_usage, network_latency) VALUES
(1, 75.5, 60.2, 500.0, 250.0, 20.5);
EOSQL

# MariaDB setup
echo "Setting up MariaDB..."
docker exec -i $(docker ps -qf "name=mariadb") mysql -u user -ppassword testdb <<-EOSQL
CREATE TABLE PerformanceMetrics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    cpu_usage FLOAT,
    memory_usage FLOAT,
    network_traffic FLOAT,
    disk_usage FLOAT,
    network_latency FLOAT
);
INSERT INTO PerformanceMetrics (student_id, cpu_usage, memory_usage, network_traffic, disk_usage, network_latency) VALUES
(1, 75.5, 60.2, 500.0, 250.0, 20.5);
EOSQL

# MongoDB setup
echo "Setting up MongoDB..."
docker exec -i $(docker ps -qf "name=mongodb") mongo testdb --eval '
db.PerformanceMetrics.insert({
    student_id: 1,
    cpu_usage: 75.5,
    memory_usage: 60.2,
    network_traffic: 500.0,
    disk_usage: 250.0,
    network_latency: 20.5
});
'

# Cassandra setup
echo "Setting up Cassandra..."
docker exec -i $(docker ps -qf "name=cassandra") cqlsh <<-EOSQL
CREATE KEYSPACE testdb WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE testdb;
CREATE TABLE PerformanceMetrics (
    student_id UUID PRIMARY KEY,
    cpu_usage float,
    memory_usage float,
    network_traffic float,
    disk_usage float,
    network_latency float
);
INSERT INTO PerformanceMetrics (student_id, cpu_usage, memory_usage, network_traffic, disk_usage, network_latency) VALUES
(now(), 75.5, 60.2, 500.0, 250.0, 20.5);
EOSQL

# Backup databases
echo "Backing up databases..."
docker exec -i $(docker ps -qf "name=postgres") pg_dump -U user -d testdb > postgres_backup.sql
docker exec -i $(docker ps -qf "name=mariadb") mysqldump -u user -ppassword testdb > mariadb_backup.sql
docker exec -i $(docker ps -qf "name=mongodb") mongoexport --db testdb --collection PerformanceMetrics --out mongo_backup.json
docker exec -i $(docker ps -qf "name=cassandra") cqlsh -e "COPY testdb.PerformanceMetrics TO '/var/lib/cassandra/data/cassandra_backup.csv'"

# Stop and remove containers
echo "Stopping and removing containers..."
docker-compose down

# Bring up containers again
echo "Bringing up containers again..."
docker-compose up -d
sleep 20

# Restore databases from backup
echo "Restoring PostgreSQL from backup..."
docker exec -i $(docker ps -qf "name=postgres") psql -U user -d testdb < postgres_backup.sql

echo "Restoring MariaDB from backup..."
docker exec -i $(docker ps -qf "name=mariadb") mysql -u user -ppassword testdb < mariadb_backup.sql

echo "Restoring MongoDB from backup..."
docker exec -i $(docker ps -qf "name=mongodb") mongoimport --db testdb --collection PerformanceMetrics --drop --file /mongo_backup.json

echo "Restoring Cassandra from backup..."
docker exec -i $(docker ps -qf "name=cassandra") cqlsh -e "COPY testdb.PerformanceMetrics FROM '/var/lib/cassandra/data/cassandra_backup.csv'"

# Log operations
echo "Logging operations..."
echo "Database operations completed on $(date)" > db_operations.log

# Shut down containers one by one
echo "Shutting down containers one by one..."
docker-compose stop postgres
docker-compose stop mariadb
docker-compose stop mongodb
docker-compose stop cassandra

echo "All operations completed successfully!"