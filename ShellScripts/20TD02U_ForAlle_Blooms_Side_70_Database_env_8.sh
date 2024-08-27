bash
#!/bin/bash

# Navn på containeren
container_name="min_mysql_database"

# Sjekk om containeren allerede kjører
if [ "$(docker ps -q -f name=$container_name)" ]; then
    echo "Containeren $container_name kjører allerede."
else
    # Start MySQL-containeren
    docker run -d \
        --name $container_name \
        -e MYSQL_ROOT_PASSWORD=mitt_sterke_passord \
        -p 3306:3306 \
        mysql:latest

    echo "MySQL-containeren $container_name er startet."
fi