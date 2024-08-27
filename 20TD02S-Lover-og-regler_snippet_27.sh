pg_dump compliance_db > compliance_backup.sql
psql compliance_db < compliance_backup.sql