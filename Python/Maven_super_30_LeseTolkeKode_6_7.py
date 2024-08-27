python
import sqlite3
from datetime import datetime

def backup_database(db_name, backup_dir):
    conn = sqlite3.connect(db_name)
    backup_name = f"{backup_dir}/backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.db"
    
    with open(backup_name, 'w') as backup_file:
        for line in conn.iterdump():
            backup_file.write('%s\n' % line)
    
    print(f"Backup created: {backup_name}")
    conn.close()

def main():
    db_name = "example.db"
    backup_dir = "backups"
    backup_database(db_name, backup_dir)

if __name__ == "__main__":
    main()