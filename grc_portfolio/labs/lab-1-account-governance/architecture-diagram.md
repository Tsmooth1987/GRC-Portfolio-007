# Lab 1: Account Governance - Architecture Diagram

Below is a text representation of the security architecture implemented in this lab. For your portfolio, consider creating a proper diagram using tools like draw.io, Lucidchart, or AWS Architecture Icons.

```
+--------------------------------------------------------------------------------------------------------------+
|                                              AWS Account                                                      |
|                                                                                                              |
|  +----------------+     +----------------+     +-------------------+     +---------------------+              |
|  |                |     |                |     |                   |     |                     |              |
|  | IAM Security   |     | CloudTrail     |     | AWS Config        |     | Security Hub        |              |
|  | - Password     |     | Logging        |     | - Config Rules    |     | - Security Standards|              |
|  |   Policy       |     | - Multi-Region |     | - Compliance      |     | - Compliance Scores |              |
|  | - Admin User   |     | - Validation   |     |   Reporting       |     | - Integrations      |              |
|  | - MFA          |     | - KMS          |     |                   |     |                     |              |
|  | - Access       |     |   Encryption   |     |                   |     |                     |              |
|  |   Analyzer     |     |                |     |                   |     |                     |              |
|  +-------+--------+     +-------+--------+     +---------+---------+     +-----------+---------+              |
|          |                      |                        |                           |                        |
|          |                      |                        |                           |                        |
|          |                      v                        v                           |                        |
|          |             +-------+------------------------+--------------+             |                        |
|          |             |                                               |             |                        |
|          |             |  S3 Buckets (Encrypted, Versioned)            |             |                        |
|          |             |  - CloudTrail Logs                            |             |                        |
|          |             |  - Config Snapshots                           |             |                        |
|          |             |                                               |             |                        |
|          |             +-----------------------------------------------+             |                        |
|          |                                                                           |                        |
|          v                                                                           v                        |
|  +-------+--------+                                               +---------------------+                     |
|  |                |                                               |                     |                     |
|  | CloudWatch     +----------------------------------------------->  SNS Topic          |                     |
|  | - Metric       |           Security Alerts                     |  (Email             |                     |
|  |   Filters      |                                               |   Notifications)    |                     |
|  | - Alarms       |                                               |                     |                     |
|  |                |                                               |                     |                     |
|  +-------+--------+                                               +---------------------+                     |
|          |                                                                                                    |
|          |                                                                                                    |
|          v                                                                                                    |
|  +----------------+                                                                                           |
|  |                |                                                                                           |
|  | AWS Budgets    |                                                                                           |
|  | - Monthly      |                                                                                           |
|  |   Budget       |                                                                                           |
|  | - Alerts       |                                                                                           |
|  |   (50/80/100%) |                                                                                           |
|  |                |                                                                                           |
|  +----------------+                                                                                           |
|                                                                                                              |
+--------------------------------------------------------------------------------------------------------------+
```

## Security Control Flow

1. **IAM Security Controls**: Enforce password policies, MFA requirements, and least privilege access
2. **CloudTrail**: Records all API activities across the AWS account
3. **CloudWatch**: Monitors CloudTrail logs for security events and triggers alarms
4. **SNS Notifications**: Sends email alerts when security events occur
5. **AWS Config**: Continuously evaluates resource configurations against security rules
6. **Security Hub**: Aggregates security findings and provides a comprehensive security score
7. **Budgets**: Monitors costs and sends alerts when thresholds are reached

## Design Principles

This architecture follows several key security design principles:

- **Defense in Depth**: Multiple layers of security controls
- **Least Privilege**: Restricting access permissions to only what is needed
- **Monitoring and Alerting**: Comprehensive logging and notification systems
- **Automation**: Automated compliance checking and reporting
- **Secure Configuration**: Baseline security settings for AWS services

## Alternative Architecture Considerations

For enterprise environments, consider these enhancements:

1. **Multi-Account Structure**: Implement AWS Organizations with separate accounts for security, audit, and workloads
2. **Centralized Logging**: Aggregate logs from multiple accounts into a dedicated logging account
3. **GuardDuty Integration**: Add threat detection capabilities
4. **Inspector**: Add vulnerability assessment for compute resources
5. **AWS Backup**: Implement automated backup policies for critical resources

## Security Services Coverage

This architecture provides coverage across multiple security domains:

- **Identity and Access Management**: IAM policies, password rules, MFA
- **Detective Controls**: CloudTrail, CloudWatch, Config
- **Infrastructure Security**: Config rules for network security
- **Data Protection**: S3 bucket protections, encryption
- **Incident Response**: Automated alerting
- **Compliance**: Config rules mapped to compliance frameworks

## Deployment Strategy

For production environments, consider:

1. **Infrastructure as Code**: Use CloudFormation/CDK to deploy and maintain
2. **CI/CD Pipeline**: Automated testing and deployment of security controls
3. **Version Control**: Track changes to security configurations
4. **Drift Detection**: Regularly check for unauthorized changes to security settings 