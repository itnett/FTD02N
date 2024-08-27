# Bash script for automated MySQL backups
#!/bin/bash
BACKUP_DIR="/backup/mysql"
MYSQL_USER="root"
MYSQL_PASSWORD="secret"

# Create a backup
mysqldump -u $MYSQL_USER -p$MYSQL_PASSWORD --all-databases > $BACKUP_DIR/backup-$(date +%F).sql

# Schedule this script to run daily using cron
# Example: 0 2 * * * /path/to/backup_script.sh