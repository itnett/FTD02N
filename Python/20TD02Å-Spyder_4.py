python
import boto3
import json
import random
import logging
import argparse
from moto import mock_s3, mock_ec2, mock_elasticbeanstalk, mock_cloudformation
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Sett opp logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- GRUNNLEGGENDE SKYTJENESTER ---
@mock_s3
def list_s3_buckets():
    """Lister alle S3-bøtter på en simulert AWS-konto."""
    s3 = boto3.client('s3')
    try:
        response = s3.list_buckets()
        logger.info("S3 Buckets:")
        for bucket in response['Buckets']:
            logger.info(f" - {bucket['Name']}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"Feil ved autentisering: {e}")
    except ClientError as e:
        logger.error(f"Klientfeil: {e}")

@mock_s3
def create_s3_bucket(bucket_name):
    """Oppretter en ny S3-bøtte på en simulert AWS-konto."""
    s3 = boto3.client('s3')
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
@mock_ec2
def deploy_iaas_instance():
    """Simulerer opprettelsen av en IaaS-instans (EC2) på en simulert AWS-konto."""
    ec2 = boto3.client('ec2')
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

@mock_elasticbeanstalk
def deploy_paas_application():
    """Simulerer opprettelsen av en PaaS-applikasjon på en simulert AWS Elastic Beanstalk."""
    beanstalk = boto3.client('elasticbeanstalk')
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

def use_saas_service(city='Oslo'):
    """Simulerer bruk av en SaaS-tjeneste ved å generere dummy værdata."""
    weather_conditions = ["Clear sky", "Few clouds", "Scattered clouds", "Broken clouds", "Shower rain", "Rain", "Thunderstorm", "Snow", "Mist"]
    weather = random.choice(weather_conditions)
    logger.info(f"Været i {city}: {weather}")

# --- SIKKERHET I SKYTJENESTER ---
@mock_s3
def enforce_s3_bucket_policy(bucket_name):
    """Implementerer en enkel S3-bøttepolicy for sikkerhet på en simulert AWS-konto."""
    s3 = boto3.client('s3')
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
@mock_cloudformation
def deploy_with_cloudformation():
    """Deploy en stack ved hjelp av AWS CloudFormation på en simulert AWS-konto."""
    cloudformation = boto3.client('cloudformation')
    try:
        template_body = json.dumps({
            "AWSTemplateFormatVersion": "2010-09-09",
            "Resources": {
                "MyEC2Instance": {
                    "Type": "AWS::EC2::Instance",
                    "Properties": {
                        "InstanceType": "t2.micro",
                        "ImageId": "ami-0abcdef1234567890"
                    }
                }
            }
        })
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

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
def run_cloud_services_examples():
    logger.info("Starter eksempler på skytjenester...")
    list_s3_buckets()
    create_s3_bucket('my-new-bucket')
    deploy_iaas_instance()
    deploy_paas_application()
    use_saas_service()
    enforce_s3_bucket_policy('my-new-bucket')
    deploy_with_cloudformation()
    logger.info("Eksempler på skytjenester fullført.")

if __name__ == "__main__":
    run_cloud_services_examples()