python
import boto3

rds = boto3.client('rds')

response = rds.delete_db_instance(
    DBInstanceIdentifier='min-mysql-database',
    SkipFinalSnapshot=True
)

print(response)