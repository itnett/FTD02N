module "vpc" {
     source = "terraform-aws-modules/vpc/aws"
     version = "2.0.0"

     name = "min-vpc"
     cidr = "10.0.0.0/16"
   }