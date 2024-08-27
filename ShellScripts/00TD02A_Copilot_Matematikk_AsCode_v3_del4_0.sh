bash
#!/bin/bash

# Start Docker containers
docker-compose up -d

# Wait for containers to be fully up and running
sleep 20

# PostgreSQL setup
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