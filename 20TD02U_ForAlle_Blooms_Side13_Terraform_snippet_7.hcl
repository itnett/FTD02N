terraform {
  backend "s3" {
    bucket = "min-terraform-state"
    key    = "infrastruktur/terraform.tfstate"
    region = "us-west-2"
  }
}