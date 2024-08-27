provider "aws" {
  region = "us-east-1"
}

module "openshift" {
  source  = "terraform-redhat/openshift/aws"
  version = "4.8.0"

  cluster_name   = "my-openshift-cluster"
  region         = "us-east-1"
  master_count   = 3
  worker_count   = 3
  ssh_key_name   = "my-ssh-key"
  base_domain    = "example.com"
}