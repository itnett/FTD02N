# Skript for å sikkerhetskopiere til flere geografiske steder med AWS S3
backup_file="/backup/skole_full_$(date +\%F).sql"
aws s3 cp $backup_file s3://backup-region-us/skole_full_$(date +\%F).sql --region us-west-1
aws s3 cp $backup_file s3://backup-region-eu/skole_full_$(date +\%F).sql --region eu-central-1

# Restore fra en spesifikk region
aws s3 cp s3://backup-region-us/skole_full_$(date +\%F).sql /restore/skole_full_$(date +\%F).sql --region us-west-1
mysql -u root -p skole < /restore/skole_full_$(date +\%F).sql