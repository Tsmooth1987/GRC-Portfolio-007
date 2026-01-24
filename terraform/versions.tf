terraform {
  required_version = ">= 1.0.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

locals {
  project = "pci-monitoring"
  common_tags = merge(
    var.tags,
    {
      Project   = "pci-monitoring"
      ManagedBy = "Terraform"
    }
  )
}
