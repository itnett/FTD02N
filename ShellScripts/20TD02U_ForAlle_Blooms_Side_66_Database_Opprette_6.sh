bash
# Eksempel på Terraform-kode for å opprette en MongoDB Atlas-kluster på flere skyer
provider "mongodbatlas" {
  public_key = "your_public_key"
  private_key = "your_private_key"
}

resource "mongodbatlas_cluster" "example" {
  project_id   = "your_project_id"
  name         = "multicloud-cluster"
  provider_backup_enabled = true

  provider_instance_size_name = "M10"
  provider_name = "AWS"
  provider_region_name = "US_WEST_2

"

  depends_on = [
    mongodbatlas_project.this
  ]
}

# Bruk Terraform til å opprette og administrere
terraform init
terraform apply