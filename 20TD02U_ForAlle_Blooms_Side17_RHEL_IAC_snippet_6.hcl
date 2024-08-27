# main.tf
module "rhel_instance" {
  source = "./modules/rhel_instance"
  instance_count = 2
  instance_type  = "t2.micro"
  ami            = "ami-0c55b159cbfafe1f0"
}