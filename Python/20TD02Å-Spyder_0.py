python
import boto3
import json
import requests
import os

# --- GRUNNLEGGENDE SKYTJENESTER ---
def list_s3_buckets():
    """Lister alle S3-bøtter på en AWS-konto."""
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")

def create_s3_bucket(bucket_name):
    """Oppretter en ny S3-bøtte."""
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=bucket_name)
    print(f"Bøtten {bucket_name} ble opprettet.")

# --- IaaS, PaaS OG SaaS ---
def deploy_iaas_instance():
    """Simulerer opprettelsen av en IaaS-instans (EC2) på AWS."""
    ec2 = boto3.client('ec2')
    response = ec2.run_instances(
        ImageId='ami-0abcdef1234567890',  # Bruk en gyldig AMI ID for din region
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    )
    print(f"EC2 Instance created with ID: {response['Instances'][0]['InstanceId']}")

def deploy_paas_application():
    """Simulerer opprettelsen av en PaaS-applikasjon på AWS Elastic Beanstalk."""
    beanstalk = boto3.client('elasticbeanstalk')
    response = beanstalk.create_application(
        ApplicationName='MySampleApp',
        Description='My sample application'
    )
    print(f"Elastic Beanstalk Application created: {response['ApplicationName']}")

def use_saas_service():
    """Simulerer bruk av en SaaS-tjeneste ved å få værdata fra en offentlig API."""
    api_key = 'din_api_nøkkel'  # Sett inn din API-nøkkel her
    city = 'Oslo'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print(f"Været i {city}: {data['weather'][0]['description']}")
    else:
        print(f"Feil ved henting av værdata for {city}")

# --- SIKKERHET I SKYTJENESTER ---
def enforce_s3_bucket_policy(bucket_name):
    """Implementerer en enkel S3-bøttepolicy for sikkerhet."""
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
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
    print(f"Policy applied to bucket: {bucket_name}")

# --- INFRASTRUCTURE AS CODE (IaC) ---
def deploy_with_cloudformation():
    """Deploy en stack ved hjelp av AWS CloudFormation."""
    cloudformation = boto3.client('cloudformation')
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
    print(f"CloudFormation stack created: {response['StackId']}")

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
def run_cloud_services_examples():
    print("Starter eksempler på skytjenester...")
    list_s3_buckets()
    create_s3_bucket('my-new-bucket')
    deploy_iaas_instance()
    deploy_paas_application()
    use_saas_service()
    enforce_s3_bucket_policy('my-new-bucket')
    deploy_with_cloudformation()
    print("Eksempler på skytjenester fullført.")

if __name__ == "__main__":
    run_cloud_services_examples()