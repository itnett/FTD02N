bash
     aws rds create-db-instance \
       --db-instance-identifier mydbinstance \
       --db-instance-class db.t2.micro \
       --engine mysql \
       --allocated-storage 20 \
       --master-username admin \
       --master-user-password password \
       --backup-retention-period 3