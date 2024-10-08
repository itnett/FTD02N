python
import boto3

rds = boto3.client('rds')

response = rds.create_db_instance(
    DBInstanceIdentifier='min-mysql-database',
    AllocatedStorage=20,  # GiB
    DBInstanceClass='db.t3.micro',
    Engine='mysql',
    MasterUsername='admin',
    MasterUserPassword='mitt_sterke_passord',
    DBName='min_database',
    VpcSecurityGroupIds=['sg-12345678'],  # Erstatt med din sikkerhetsgruppe-ID
    PubliclyAccessible=True,  # Hvis du vil ha tilgang utenfra
)

print(response)