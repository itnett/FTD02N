bash
# Bash script for å sjekke SSL og logging status
#!/bin/bash
# Sjekk SSL-status
ssl_status=$(mysql -u root -e "SHOW VARIABLES LIKE 'have_ssl';" | grep 'have_ssl' | awk '{print $2}')
echo "SSL Status: $ssl_status"

# Sjekk logging status
log_status=$(mysql -u root -e "SHOW VARIABLES LIKE 'general_log';" | grep 'general_log' | awk '{print $2}')
echo "General Log Status: $log_status"

# Planlegg dette scriptet til å kjøre regelmessig ved hjelp av cron
# Eksempel: 0 0 * * * /path/to/security_check.sh