bash
     aws dynamodb create-table \
       --table-name Students \
       --attribute-definitions \
         AttributeName=StudentID,AttributeType=S \
       --key-schema \
         AttributeName=StudentID,KeyType=HASH \
       --provisioned-throughput \
         ReadCapacityUnits=5,WriteCapacityUnits=5