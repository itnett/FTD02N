bash
#!/bin/bash

# Spør brukeren om input
read -p "Enter PostgreSQL username: " PG_USER
read -sp "Enter PostgreSQL password: " PG_PASSWORD
echo ""
read -p "Enter PostgreSQL database name: " PG_DB
read -p "Enter MariaDB/MySQL username: " MYSQL_USER
read -sp "Enter MariaDB/MySQL password: " MYSQL_PASSWORD
echo ""
read -p "Enter MariaDB/MySQL database name: " MYSQL_DB

# Sett miljøvariabler
export PG_USER PG_PASSWORD PG_DB MYSQL_USER MYSQL_PASSWORD MYSQL_DB

# Start Docker containers
docker-compose up -d

# Vent til containere er oppe og kjører
sleep 20

# Funksjon for feilhåndtering
handle_error() {
    echo "Error occurred at $1"
    exit 1
}

# PostgreSQL setup
echo "Setting up PostgreSQL..."
docker exec -i $(docker ps -qf "name=postgres") psql -U $PG_USER -d $PG_DB <<-EOSQL || handle_error "PostgreSQL setup"
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
docker exec -i $(docker ps -qf "name=mariadb") mysql -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DB <<-EOSQL || handle_error "MariaDB setup"
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
docker exec -i $(docker ps -qf "name=mongodb") mongo $PG_DB --eval '
db.PerformanceMetrics.insert({
    student_id: 1,
    cpu_usage: 75.5,
    memory_usage: 60.2,
    network_traffic: 500.0,
    disk_usage: 250.0,
    network_latency: 20.5
});
' || handle_error "MongoDB setup"

# Cassandra setup
echo "Setting up Cassandra..."
docker exec -i $(docker ps -qf "name=cassandra") cqlsh <<-EOSQL || handle_error "Cassandra setup"
CREATE KEYSPACE $PG_DB WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE $PG_DB;
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
docker exec -i $(docker ps -qf "name=postgres") pg_dump -U $PG_USER -d $PG_DB > postgres_backup.sql || handle_error "PostgreSQL backup"
docker exec -i $(docker ps -qf "name=mariadb") mysqldump -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DB > mariadb_backup.sql || handle_error "MariaDB backup"
docker exec -i $(docker ps -qf "name=mongodb") mongoexport --db $PG_DB --collection PerformanceMetrics --out mongo_backup.json || handle_error "MongoDB backup"
docker exec -i $(docker ps -qf "name=cassandra") cqlsh -e "COPY $PG_DB.PerformanceMetrics TO '/var/lib/cassandra/data/cassandra_backup.csv'" || handle_error "Cassandra backup"

# Stop and remove containers
echo "Stopping and removing containers..."
docker-compose down

# Bring up containers again
echo "Bringing up containers again..."
docker-compose up -d
sleep 20

# Restore databases from backup
echo "Restoring PostgreSQL from backup..."
docker exec -i $(docker ps -qf "name=postgres") psql -U $PG_USER -d $PG_DB < postgres_backup.sql || handle_error "PostgreSQL restore"

echo "Restoring MariaDB from backup..."
docker exec -i $(docker ps -qf "name=mariadb") mysql -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DB < mariadb_backup.sql || handle_error "MariaDB restore"

echo "Restoring MongoDB from backup..."
docker exec -i $(docker ps -qf "name=mongodb") mongoimport --db $PG_DB --collection PerformanceMetrics --drop --file mongo_backup.json || handle_error "MongoDB restore"

echo "Restoring Cassandra from backup..."
docker exec -i $(docker ps -qf "name=cassandra") cqlsh -e "COPY $PG_DB.PerformanceMetrics FROM '/var/lib/cassandra/data/cassandra_backup.csv'" || handle_error "Cassandra restore"

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