# Create a new VPC network
gcloud compute networks create my-vpc --subnet-mode=custom

# Create a new subnet
gcloud compute networks subnets create my-subnet \
    --network=my-vpc \
    --range=10.0.0.0/24