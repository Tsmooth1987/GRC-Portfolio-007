# GRC Portfolio

Welcome to my Governance, Risk, and Compliance (GRC) portfolio! This repository showcases my work in cloud security and compliance automation.

## Directory Structure

- `projects/`: Production-ready tools and scripts
  - `aws-security/`: AWS security automation tools
  - `automation/`: General automation scripts

- `labs/`: Learning materials and exercises
  - `python-exercises/`: Python coding practice
  - `aws-tutorials/`: AWS service walkthroughs

- `docs/`: Documentation and reports
  - `reports/`: Generated reports and logs
  - `study-materials/`: Study guides and references
EOLmkdir -p GRC-Portfolio/docs/study-materialsmv /Users/terencewebster/Desktop/GRC/PYTHON/STUDY_PLAN.md \
   /Users/terencewebster/Desktop/GRC/PYTHON/STUDY_PLAN_TEMPLATE.md \
   /Users/terencewebster/Desktop/GRC/PYTHON/README-EC2-SG-AUDITOR.md \
   GRC-Portfolio/docs/study-materials/# Check the structure
tree GRC-Portfolio/cd /Users/terencewebster/Desktop/GRC/Portfolio/GRC-Portfolio/projects/aws-security
python3 sg_auditor.py --profile default --output excel
# Check if Security Hub is enabled
aws securityhub describe-hub

# Get a summary of findings
aws securityhub get-findings --max-items 10# List all S3 buckets and their public access settings
for bucket in $(aws s3 ls | awk '{print $3}'); do
    echo "=== Bucket: $bucket ==="
    aws s3api get-bucket-acl --bucket $bucket
    aws s3api get-bucket-policy-status --bucket $bucket 2>/dev/null || echo "No bucket policy"
    echo "------------------------"
done# Get a summary of IAM users and their access
aws iam generate-credential-report
aws iam get-credential-report --output text | base64 --decodecd /Users/terencewebster/Desktop/GRC/Portfolio/GRC-Portfolio/projects/aws-security
ls -l
python3 sg_auditor.py --profile default --output excel
ls -l *.xlsx
# Check security groups
aws ec2 describe-security-groups --query 'SecurityGroups[*].[GroupName,GroupId,Description]' --output table

# Check for open security groups (0.0.0.0/0)
aws ec2 describe-security-groups --filters Name=ip-permission.cidr,Values='0.0.0.0/0' --query 'SecurityGroups[*].[GroupName,GroupId]' --output table# Check security groups
aws ec2 describe-security-groups --query 'SecurityGroups[*].[GroupName,GroupId,Description]' --output table

# Check for open security groups (0.0.0.0/0)
aws ec2 describe-security-groups --filters Name=ip-permission.cidr,Values='0.0.0.0/0' --query 'SecurityGroups[*].[GroupName,GroupId]' --output table# List all S3 buckets
aws s3 ls

# Check public access settings for each bucket
for bucket in $(aws s3 ls | awk '{print $3}'); do
    echo "=== Checking $bucket ==="
    aws s3api get-public-access-block --bucket $bucket 2>/dev/null || echo "No public access block configuration"
    echo "------------------------"
done# Generate and view credential report
aws iam generate-credential-report
sleep 5  # Wait for report to generate
aws iam get-credential-report --output text | base64 --decode# Check for MFA status
aws iam get-account-summary | grep -E 'AccountMFAEnabled|AccountAccessKeysPresent'

# Check for root account activity
aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=root --max-items 5# Run this command to find security groups allowing access from anywhere (0.0.0.0/0)
aws ec2 describe-security-groups \
    --filters Name=ip-permission.cidr,Values='0.0.0.0/0' \
    --query 'SecurityGroups[*].[GroupName,GroupId,Description]' \
    --output table# Replace SECURITY_GROUP_ID with an actual group ID from the previous command
aws ec2 describe-security-groups \
    --group-ids SECURITY_GROUP_ID \
    --query 'SecurityGroups[0].IpPermissions' \
    --output json# Check for open SSH (port 22)
aws ec2 describe-security-groups \
    --filters Name=ip-permission.from-port,Values=22 Name=ip-permission.cidr,Values='0.0.0.0/0' \
    --query 'SecurityGroups[*].[GroupName,GroupId]' \
    --output table

# Check for open RDP (port 3389)
aws ec2 describe-security-groups \
    --filters Name=ip-permission.from-port,Values=3389 Name=ip-permission.cidr,Values='0.0.0.0/0' \
    --query 'SecurityGroups[*].[GroupName,GroupId]' \
    --output table# Check for open SSH (port 22)
aws ec2 describe-security-groups \
    --filters Name=ip-permission.from-port,Values=22 Name=ip-permission.cidr,Values='0.0.0.0/0' \
    --query 'SecurityGroups[*].[GroupName,GroupId]' \
    --output table

# Check for open RDP (port 3389)
aws ec2 describe-security-groups \
    --filters Name=ip-permission.from-port,Values=3389 Name=ip-permission.cidr,Values='0.0.0.0/0' \
    --query 'SecurityGroups[*].[GroupName,GroupId]' \
    --output table# List all S3 buckets and their public access settings
for bucket in $(aws s3 ls | awk '{print $3}'); do
    echo "=== Bucket: $bucket ==="
    # Check if bucket is publicly accessible
    aws s3api get-public-access-block --bucket $bucket 2>/dev/null || echo "No public access block configuration"
    # Check bucket policy
    aws s3api get-bucket-policy-status --bucket $bucket 2>/dev/null || echo "No bucket policy"
    echo "------------------------"
done# Check for users without MFA
aws iam list-users --query 'Users[*].UserName' | jq -r '.[]' | while read user; do
    mfa_devices=$(aws iam list-mfa-devices --user-name $user --query 'MFADevices' --output text)
    [ -z "$mfa_devices" ] && echo "User $user has no MFA device"
done

# Check for old access keys (older than 90 days)
aws iam list-users --query 'Users[*].UserName' | jq -r '.[]' | while read user; do
    aws iam list-access-keys --user-name $user --query 'AccessKeyMetadata[?CreateDate<`'$(date -v-90d +%Y-%m-%d)'`]' --output text
done# Check for users without MFA
aws iam list-users --query 'Users[*].UserName' | jq -r '.[]' | while read user; do
    mfa_devices=$(aws iam list-mfa-devices --user-name $user --query 'MFADevices' --output text)
    [ -z "$mfa_devices" ] && echo "User $user has no MFA device"
done

# Check for old access keys (older than 90 days)
aws iam list-users --query 'Users[*].UserName' | jq -r '.[]' | while read user; do
    aws iam list-access-keys --user-name $user --query 'AccessKeyMetadata[?CreateDate<`'$(date -v-90d +%Y-%m-%d)'`]' --output text
done# Navigate to your portfolio directory
cd /Users/terencewebster/Desktop/GRC/Portfolio/GRC-Portfolio

# Initialize git (if not already done)
git init

# Add GitHub as remote (replace with your GitHub URL)
git remote add origin https://github.com/yourusername/grc-security-audit.git

# Create directory structure
mkdir -p findings/{security_groups,s3,iam,remediation}# Example: Create a finding template
cat > findings/security_groups/open_ssh_ports.md << 'EOL'
# Open SSH Port Finding

## Details
- **Severity**: High
- **Resource Type**: Security Group
- **Resource ID**: [SG-ID]
- **Region**: us-east-1
- **Discovered**: $(date +%Y-%m-%d)

## Description
SSH port (22) is open to the internet (0.0.0.0/0).

## Risk
Potential unauthorized access to EC2 instances.

## Evidence
```json
[Paste output from aws ec2 describe-security-groups here]
cat > FINDINGS_SUMMARY.md << 'EOL'
# Security Audit Summary

## Overview
- **Date**: $(date +%Y-%m-%d)
- **Account ID**: [Your AWS Account ID]
- **Auditor**: [Your Name]

## Findings Summary
| Severity | Count |
|----------|-------|
| Critical | 0     |
| High     | 0     |
| Medium   | 0     |
| Low      | 0     |

## Detailed Findings
1. [Critical] Open SSH Ports
2. [High] Public S3 Buckets
3. [Medium] IAM Users Without MFA

## Next Steps
1. Review high and critical findings
2. Implement remediation steps
3. Schedule follow-up audit
EOL# Add all files
git add .

# Commit changes
git commit -m "Initial security audit findings"

# Push to GitHub
git push -u origin maincat > REMEDIATION_PLAN.md << 'EOL'
# Security Remediation Plan

## Immediate Actions (24-48 hours)
1. [ ] Restrict SSH access to specific IPs
2. [ ] Enable MFA for all IAM users
3. [ ] Review and update S3 bucket policies

## Short-term (1-2 weeks)
1. [ ] Implement AWS Config rules
2. [ ] Set up CloudTrail alerts
3. [ ] Conduct IAM access review

## Long-term (1-3 months)
1. [ ] Implement infrastructure as code
2. [ ] Set up automated security scanning
3. [ ] Conduct security training
EOLpwd
ls -l# Navigate to the project directory
cd /Users/terencewebster/Desktop/GRC/Portfolio/GRC-Portfolio/projects/aws-security

# Check if sg_auditor.py exists
ls -l sg_auditor.pypython3 sg_auditor.py --help# Create a basic security group auditor
cat > sg_auditor.py << 'EOL'
import boto3
import argparse
from datetime import datetime

def audit_security_groups(profile='default', region='us-east-1'):
    """Basic security group auditor"""
    print(f"Starting security group audit - {datetime.now()}")
    session = boto3.Session(profile_name=profile, region_name=region)
    ec2 = session.client('ec2')
    
    try:
        response = ec2.describe_security_groups()
        print("\nFound security groups:")
        for group in response['SecurityGroups']:
            print(f"- {group['GroupName']} ({group['GroupId']})")
        
        print("\nChecking for open ports...")
        # Add your security checks here
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='AWS Security Group Auditor')
    parser.add_argument('--profile', default='default', help='AWS profile name')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    args = parser.parse_args()
    
    audit_security_groups(args.profile, args.region)
