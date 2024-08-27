bash
#!/bin/bash

LOG_DB="server_log.db"

# Oppretter SQLite-tabell for logging hvis den ikke finnes
sqlite3 $LOG_DB "CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, event TEXT);"

# Logger en hendelse til SQLite
log_event() {
    local event=$1
    local timestamp=$(date --iso-8601=seconds)
    sqlite3 $LOG_DB "INSERT INTO logs (timestamp, event) VALUES ('$timestamp', '$event');"
}

# Leser loggene fra SQLite-databasen
read_logs() {
    sqlite3 $LOG_DB "SELECT * FROM logs;"
}

# Hovedskript
main() {
    echo "Server Maintenance Log"
    
    # Logger en hendelse
    log_event "System backup completed successfully."
    
    # Leser loggene
    read_logs
}

main