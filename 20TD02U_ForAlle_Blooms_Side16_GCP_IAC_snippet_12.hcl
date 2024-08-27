resource "google_logging_project_sink" "gcs_logging" {
  name        = "gcs-logging"
  destination = "storage.googleapis.com/my-log-bucket"
  filter      = "resource.type=gcs_bucket"
}