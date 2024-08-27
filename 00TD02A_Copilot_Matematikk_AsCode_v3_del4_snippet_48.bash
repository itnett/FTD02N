#!/bin/bash

GRAFANA_URL="http://admin:admin@localhost:3000"
POSTGRES_DATASOURCE='{
  "name": "PostgreSQL",
  "type": "postgres",
  "access": "proxy",
  "url": "postgres:5432",
  "database": "testdb",
  "user": "user",
  "password": "password",
  "jsonData": {
    "sslmode": "disable"
  }
}'

MYSQL_DATASOURCE='{
  "name": "MariaDB",
  "type": "mysql",
  "access": "proxy",
  "url": "mariadb:3306",
  "database": "testdb",
  "user": "user",
  "password": "password"
}'

MONGODB_DATASOURCE='{
  "name": "MongoDB",
  "type": "mongodb",
  "access": "proxy",
  "url": "mongodb://mongo:27017",
  "database": "testdb"
}'

CASSANDRA_DATASOURCE='{
  "name": "Cassandra",
  "type": "grafana-cassandra-datasource",
  "access": "proxy",
  "url": "cassandra:9042",
  "database": "testdb"
}'

# Wait for Grafana to start
sleep 20

# Add PostgreSQL datasource
curl -X POST -H "Content-Type: application/json" -d "${POSTGRES_DATASOURCE}" ${GRAFANA_URL}/api/datasources

# Add MariaDB datasource
curl -X POST -H "Content-Type: application/json" -d "${MYSQL_DATASOURCE}" ${GRAFANA_URL}/api/datasources

# Add MongoDB datasource
curl -X POST -H "Content-Type: application/json" -d "${MONGODB_DATASOURCE}" ${GRAFANA_URL}/api/datasources

# Add Cassandra datasource
curl -X POST -H "Content-Type: application/json" -d "${CASSANDRA_DATASOURCE}" ${GRAFANA_URL}/api/datasources