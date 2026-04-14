terraform {
  required_version = ">= 1.8.0"
}

variable "project" { type = string }

output "note" {
  value = "Terraform module scaffold for cluster addons, DNS/TLS, secrets and monitoring."
}
