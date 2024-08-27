module "gce_instance" {
  source         = "terraform-google-modules/vm/google"
  project_id     = var.project_id
  zone           = var.zone
  name           = "terraform-instance"
  machine_type   = "n1-standard-1"
  image          = "debian-cloud/debian-9"
  network        = "default"
  subnetwork     = "default"
}