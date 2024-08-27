bash
#!/bin/bash

DB_NAME="example.db"
BACKUP_DIR="backups"

# Sikkerhetskopier database
backup_database() {
    local timestamp=$(date +"%Y%m%d%H%M%S")
    sqlite3 $DB_NAME ".backup '$BACKUP_DIR/backup_$timestamp.db'"
    echo "Backup created: backup_$timestamp.db"
}

# Opprett bruker
create_user() {
    local username=$1
    local password=$2
    sqlite3 $DB_NAME "INSERT INTO users (username, password) VALUES ('$username', '$password');"
    echo "User $username created."
}

# Hovedskript
main() {
    mkdir -p $BACKUP_DIR
    
    # Oppretter brukertabellen hvis den ikke finnes
    sqlite3 $DB_NAME "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT);"
    
    # Opprett bruker og lag backup
    create_user "newuser" "password123"
    backup_database
}

main