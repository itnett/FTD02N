aws ec2 create-vpc --cidr-block 10.0.0.0/16
   aws ec2 create-subnet --vpc-id vpc-12345678 --cidr-block 10.0.1.0/24
   aws ec2 create-internet-gateway
   aws ec2 attach-internet-gateway --vpc-id vpc-12345678 --internet-gateway-id igw-12345678
   aws ec2 create-route-table --vpc-id vpc-12345678
   aws ec2 create-route --route-table-id rtb-12345678 --destination-cidr-block 0.0.0.0/0 --gateway-id igw-12345678