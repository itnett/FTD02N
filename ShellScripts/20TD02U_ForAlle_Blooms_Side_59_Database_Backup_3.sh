bash
# Script for å måle tiden det tar å gjenopprette en database
start_time=$(date +%s)
mysql -u root -p skole < skole_backup.sql
end_time=$(date +%s)
restore_time=$((end_time - start_time))
echo "Restore tid: $restore_time sekunder"