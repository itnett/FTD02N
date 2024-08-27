#!/bin/bash

# Automatisk backup av MySQL-database
backup_dir="/backup/mysql"
timestamp=$(date +"%F")
backup_file="$backup_dir/skole_$timestamp.sql"

mkdir -p "$backup_dir"
mysqldump -u root -p'yourpassword' skole > "$backup_file"

# Automatisert restore (for testformål)
mysql -u root -p'yourpassword' skole < "$backup_file"