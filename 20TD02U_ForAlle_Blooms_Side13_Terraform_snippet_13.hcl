provider "vault" {
  address = "https://vault.example.com"
}

data "vault_generic_secret" "eksempel_hemmelig" {
  path = "secret/infra/hemmelig"
}