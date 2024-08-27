resource "google_secret_manager_secret" "my_secret" {
  secret_id = "my-secret"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "secret_version" {
  secret      = google_secret_manager_secret.my_secret.id
  secret_data = "my-secret-value"
}