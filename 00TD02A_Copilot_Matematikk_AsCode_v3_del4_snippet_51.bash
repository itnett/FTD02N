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

# ... (rest of the script)