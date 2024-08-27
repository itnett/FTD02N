#!/bin/bash

GRAFANA_URL="http://admin:admin@localhost:3000"

# Funksjon for feilhåndtering
handle_error() {
    echo "Error occurred at $1"
    exit 1
}

# Add PostgreSQL datasource
POSTGRES_DATASOURCE='{
  "name": "PostgreSQL",
  "type": "postgres",
  "access": "proxy",
  "url": "postgres:5432",
  "database": "'$PG_DB'",
  "user": "'$PG_USER'",
  "password": "'$PG_PASSWORD'",
  "jsonData": {
    "sslmode": "disable"
  }
}'

curl -X POST -H "Content-Type: application/json" -d "${POSTGRES_DATASOURCE}" ${GRAFANA_URL}/api/datasources || handle_error "Adding PostgreSQL datasource"

# Add MariaDB datasource
MYSQL_DATASOURCE='{
  "name": "MariaDB",
  "type": "mysql",
  "access": "proxy",
  "url": "mariadb:3306",
  "database": "'$MYSQL_DB'",
  "user": "'$MYSQL_USER'",
  "password": "'$MYSQL_PASSWORD'"
}'

curl -X POST -H "Content-Type: application/json" -d "${MYSQL_DATASOURCE}" ${GRAFANA_URL}/api/datasources || handle_error "Adding MariaDB datasource"

# Add MongoDB datasource
MONGODB_DATASOURCE='{
  "name": "MongoDB",
  "type": "mongodb",
  "access": "proxy",
  "url": "mongodb://mongo:27017",
  "database": "'$PG

_DB'"
}'

curl -X POST -H "Content-Type: application/json" -d "${MONGODB_DATASOURCE}" ${GRAFANA_URL}/api/datasources || handle_error "Adding MongoDB datasource"

# Add Cassandra datasource
CASSANDRA_DATASOURCE='{
  "name": "Cassandra",
  "type": "grafana-cassandra-datasource",
  "access": "proxy",
  "url": "cassandra:9042",
  "database": "'$PG_DB'"
}'

curl -X POST -H "Content-Type: application/json" -d "${CASSANDRA_DATASOURCE}" ${GRAFANA_URL}/api/datasources || handle_error "Adding Cassandra datasource"

echo "All datasources added successfully!"