# S3 Bucket for Terraform State
resource "aws_s3_bucket" "terraform_state" {
  bucket = "pci-monitoring-tfstate-43842c25"
  force_destroy = false
}

# Enable versioning for the S3 bucket
resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Enable server-side encryption for the S3 bucket
resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# DynamoDB Table for State Locking
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  # Add tags if needed
  tags = {
    Name        = "Terraform Lock Table"
    Environment = "dev"
    Project     = "pci-monitoring"
    ManagedBy   = "Terraform"
  }
}
