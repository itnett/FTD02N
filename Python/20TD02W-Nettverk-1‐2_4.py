python
import boto3

ec2 = boto3.resource('ec2')

# Create a new VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc.create_tags(Tags=[{"Key": "Name", "Value": "my_vpc"}])
vpc.wait_until_available()

# Create a subnet
subnet = vpc.create_subnet(CidrBlock='10.0.1.0/24')

# Create an internet gateway and attach it to the VPC
internet_gateway = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=internet_gateway.id)

# Create a route table and a public route
route_table = vpc.create_route_table()
route = route_table.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway.id
)

# Associate the route table with the subnet
route_table.associate_with_subnet(SubnetId=subnet.id)