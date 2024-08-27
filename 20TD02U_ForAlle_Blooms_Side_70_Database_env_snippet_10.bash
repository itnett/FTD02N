#!/bin/bash

container_name="min_mysql_database"

# Stopp og fjern containeren
docker stop $container_name
docker rm $container_name

echo "MySQL-containeren $container_name er stoppet og fjernet."