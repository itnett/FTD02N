bash
# Skript for å sjekke om alle planlagte backups er fullført og varsle ved feil
backup_file="/backup/skole_full_$(date +\%F).sql"
if [ -f "$backup_file" ]; then
    echo "Backup fullført: $backup_file"
else
    echo "Feil: Backup mangler!" | mail -s "Backup Feil" admin@domain.com
fi