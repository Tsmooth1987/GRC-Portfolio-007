terraform {
  backend "s3" {
    bucket         = "pci-monitoring-tfstate-43842c25"
    key            = "pci-monitoring/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}