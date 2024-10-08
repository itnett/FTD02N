python
import boto3
import json
import requests
import os
import logging
import argparse
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Konfigurer boto3 til å bruke LocalStack (for lokal simulering)
LOCALSTACK = os.environ.get('LOCALSTACK', 'false').lower() == 'true'
if LOCALSTACK:
    endpoint_url = 'http://localhost:4566'
    boto3.setup_default_session(
        aws_access_key_id='test',
        aws_secret_access_key='test',
        region_name='us-east-1'
    )
else:
    endpoint_url = None

# Sett opp logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- GRUNNLEGGENDE SKYTJENESTER ---
def list_s3_buckets():
    """Lister alle S3-bøtter på en AWS-konto."""
    s3 = boto3.client('s3', endpoint_url=endpoint_url)
    try:
        response = s3.list_buckets()
        logger.info("S3 Buckets:")
        for bucket in response['Buckets']:
            logger.info(f" - {bucket['Name']}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"Feil ved autentisering: {e}")
    except ClientError as e:
        logger.error(f"Klientfeil: {e}")

def create_s3_bucket(bucket_name):
    """Oppretter en ny S3-bøtte."""
    s3 = boto3.client('s3', endpoint_url=endpoint_url)
    try:
        if not bucket_name.islower() or ' ' in bucket_name:
            raise ValueError("Bucket navn må være i små bokstaver og uten mellomrom.")
        response = s3.create_bucket(Bucket=bucket_name)
        logger.info(f"Bøtten {bucket_name} ble opprettet.")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"Feil ved autentisering: {e}")
    except ClientError as e:
        logger.error(f"Klientfeil: {e}")
    except ValueError as e:
        logger.error(f"Valideringsfeil: {e}")

# --- IaaS, PaaS OG SaaS ---
def deploy_iaas_instance():
    """Simulerer opprettelsen av en IaaS-instans (EC2) på AWS."""
    ec2 = boto3.client('ec2', endpoint_url=endpoint_url)
    try:
        response = ec2.run_instances(
            ImageId='ami-0abcdef1234567890',  # Bruk en gyldig AMI ID for din region
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1
        )
        logger.info(f"EC2 Instance created with ID: {response['Instances'][0]['InstanceId']}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"Feil ved autentisering: {e}")
    except ClientError as e:
        logger.error(f"Klientfeil: {e}")

def deploy_paas_application():
    """Simulerer opprettelsen av en PaaS-applikasjon på AWS Elastic Beanstalk."""
    beanstalk = boto3.client('elasticbeanstalk', endpoint_url=endpoint_url)
    try:
        response = beanstalk.create_application(
            ApplicationName='MySampleApp',
            Description='My sample application'
        )
        logger.info(f"Elastic Beanstalk Application created: {response['ApplicationName']}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"Feil ved autentisering: {e}")
    except ClientError as e:
        logger.error(f"Klientfeil: {e}")

def use_saas_service(api_key, city='Oslo'):
    """Simulerer bruk av en SaaS-tjeneste ved å få værdata fra en offentlig API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            logger.info(f"Været i {city}: {data['weather'][0]['description']}")
        else:
            logger.error(f"Feil ved henting av værdata for {city}: {data}")
    except requests.RequestException as e:
        logger.error(f"HTTP-feil: {e}")

# --- SIKKERHET I SKYTJENESTER ---
def enforce_s3_bucket_policy(bucket_name):
    """Implementerer en enkel S3-bøttepolicy for sikkerhet."""
    s3 = boto3.client('s3', endpoint_url=endpoint_url)
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }]
    }
    bucket_policy = json.dumps(bucket_policy)
    try:
        s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
        logger.info(f"Policy applied to bucket: {bucket_name}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"Feil ved autentisering: {e}")
    except ClientError as e:
        logger.error(f"Klientfeil: {e}")

# --- INFRASTRUCTURE AS CODE (IaC) ---
def deploy_with_cloudformation():
    """Deploy en stack ved hjelp av AWS CloudFormation."""
    cloudformation = boto3.client('cloudformation', endpoint_url=endpoint_url)
    try:
        with open('cloudformation_template.json', 'r') as template_file:
            template_body = template_file.read()
        response = cloudformation.create_stack(
            StackName='MyStack',
            TemplateBody=template_body,
            Parameters=[
                {
                    'ParameterKey': 'InstanceType',
                    'ParameterValue': 't2.micro'
                },
            ]
        )
        logger.info(f"CloudFormation stack created: {response['StackId']}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"Feil ved autentisering: {e}")
    except ClientError as e:
        logger.error(f"Klientfeil: {e}")
    except FileNotFoundError as e:
        logger.error(f"Fil ikke funnet: {e}")

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
def run_cloud_services_examples(api_key):
    logger.info("Starter eksempler på skytjenester...")
    list_s3_buckets()
    create_s3_bucket('my-new-bucket')
    deploy_iaas_instance()
    deploy_paas_application()
    use_saas_service(api_key)
    enforce_s3_bucket_policy('my-new-bucket')
    deploy_with_cloudformation()
    logger.info("Eksempler på skytjenester fullført.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Kjør eksempler på skytjenester.')
    parser.add_argument('--api_key', type=str, required=True, help='API-nøkkel for SaaS-tjenesten')
    args = parser.parse_args()
    
    run_cloud_services_examples(args.api_key)