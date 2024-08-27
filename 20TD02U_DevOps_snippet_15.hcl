# Definer variable for miljøer
   variable "environment" {
     type    = string
     default = "dev"
   }

   # Bruk variabelen for å angi ressurser
   resource "aws_instance" "example" {
     count         = var.environment == "prod" ? 3 : 1
     ami           = "ami-0c55b159cbfafe1f0"
     instance_type = "t2.micro"

     tags = {
       Name = "example-${var.environment}"
     }
   }