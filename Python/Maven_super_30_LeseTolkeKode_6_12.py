python
import os
import logging
import sqlite3
from datetime import datetime

# Setup logging
log_filename = 'server_log.db'  # Bruker SQLite database for logging
conn = sqlite3.connect(log_filename)
cursor = conn.cursor()

# Oppretter loggtabell om den ikke eksisterer
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    event TEXT
)
''')

def log_event(event):
    """
    Logger en hendelse i SQLite-databasen med tidsstempel.
    """
    timestamp = datetime.now().isoformat()
    cursor.execute("INSERT INTO logs (timestamp, event) VALUES (?, ?)", (timestamp, event))
    conn.commit()

def check_disk_space():
    """
    Simulerer en sjekk av diskplass.
    """
    total, used, free = 100, 75, 25  # Eksempelverdier i GB
    event = f"Disk space check: Total: {total}GB, Used: {used}GB, Free: {free}GB"
    log_event(event)
    return total, used, free

def read_logs():
    """
    Leser og skriver ut loggene fra SQLite-databasen.
    """
    cursor.execute("SELECT * FROM logs")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    print("Server Maintenance Log")
    
    # Sjekker diskplass
    check_disk_space()
    
    # Simulerer flere serverhendelser
    log_event("System backup completed successfully.")
    log_event("Detected unauthorized access attempt.")
    
    # Leser loggene
    read_logs()

if __name__ == "__main__":
    main()