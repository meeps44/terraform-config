terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

variable "do_token" {}
variable "pvt_key" {}
variable "location" {
  description = "The location/region where the droplet will be created."
  default     = "lon1"
}

provider "digitalocean" {
  token = var.do_token
}

data "digitalocean_ssh_key" "new-key" {
  name = "new-key"
}
