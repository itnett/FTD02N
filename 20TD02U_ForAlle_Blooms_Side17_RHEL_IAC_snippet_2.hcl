provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "rhel_instance" {
  ami           = "ami-0c55b159cbfafe1f0" # RHEL AMI
  instance_type = "t2.micro"

  tags = {
    Name = "RHEL-Instance"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd",
      "sudo systemctl start httpd",
      "sudo systemctl enable httpd"
    ]
  }
}