bash
# Cron-jobb for å ta en automatisk full backup hver søndag kl. 02:00
0 2 * * 0 mysqldump -u root -p skole > /backup/skole_backup_$(date +\%F).sql

# Cron-jobb for å ta en inkrementell backup hver dag kl. 02:00
0 2 * * * rsync -av --progress /var/lib/mysql /backup/mysql_incr_$(date +\%F)