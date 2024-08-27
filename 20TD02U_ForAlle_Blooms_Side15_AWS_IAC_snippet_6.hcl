terraform {
  backend "s3" {
    bucket         = "terraform-state-bucket"
    key            = "global/s3/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "terraform-locks"
  }
}