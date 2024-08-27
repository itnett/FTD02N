# AWS CLI for å opprette en RDS-database
aws rds create-db-instance \
    --db-instance-identifier mydatabase \
    --db-instance-class db.t2.micro \
    --engine mysql \
    --allocated-storage 20 \
    --master-username admin \
    --master-user-password secret99 \
    --backup-retention-period 7