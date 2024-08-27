# Fullstendig backup til lokal og ekstern lagring (f.eks., AWS S3)
mysqldump -u root -p skole > /backup/skole_full_$(date +\%F).sql
aws s3 cp /backup/skole_full_$(date +\%F).sql s3://mybackupbucket/skole_full_$(date +\%F).sql

# Verifikasjon av backup-integritet ved å sammenligne filstørrelse eller kontrollsum
local_checksum=$(md5sum /backup/skole_full_$(date +\%F).sql | awk '{ print $1 }')
remote_checksum=$(aws s3api head-object --bucket mybackupbucket --key skole_full_$(date +\%F).sql --query Checksum)
if [ "$local_checksum" == "$remote_checksum" ]; then
    echo "Backup integritet verifisert."
else
    echo "Backup integritet feil."
fi