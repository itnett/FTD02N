resource "google_project_iam_member" "binding" {
  project = "my-gcp-project"
  role    = "roles/viewer"
  member  = "user:myuser@example.com"
}