python
import json
import boto3

def lambda_handler(event, context):
    temperature_data = json.loads(event['body'])
    # Prosessere temperaturdataene her
    print(f"Received temperature data: {temperature_data}")
    
    # Lagre dataene i en S3-bøtte
    s3 = boto3.client('s3')
    s3.put_object(Bucket='temperature-data-bucket', Key='data.json', Body=json.dumps(temperature_data))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data received and processed')
    }