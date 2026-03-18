#!/usr/bin/env python3
"""
Import GitLab SAST/DAST findings to AWS Security Hub
"""

import json
import boto3
import datetime
import os

def map_severity(severity):
    """Map GitLab severity to Security Hub severity"""
    severity_map = {
        'CRITICAL': 'CRITICAL',
        'HIGH': 'HIGH', 
        'MEDIUM': 'MEDIUM',
        'LOW': 'LOW',
        'INFO': 'INFORMATIONAL'
    }
    return severity_map.get(severity.upper(), 'MEDIUM')

def map_normalized_severity(severity):
    """Map severity to normalized score (0-100)"""
    severity_map = {
        'CRITICAL': 90,
        'HIGH': 70,
        'MEDIUM': 50,
        'LOW': 30,
        'INFO': 10
    }
    return severity_map.get(severity.upper(), 50)

def import_sast_findings(securityhub, report_file, aws_region, aws_account_id, gitlab_project, gitlab_commit_sha, gitlab_branch):
    """Import SAST findings to Security Hub"""
    try:
        with open(report_file, 'r') as f:
            findings = json.load(f)
        
        security_hub_findings = []
        
        if 'results' in findings:
            for result in findings['results']:
                finding = {
                    'SchemaVersion': '2018-10-08',
                    'Id': f"sast-{result.get('test_name', 'unknown')}-{datetime.datetime.now().isoformat()}",
                    'ProductArn': f"arn:aws:securityhub:{aws_region}:{aws_account_id}:product/codescanning/gitlab-sast",
                    'ProductName': 'GitLab SAST',
                    'CompanyName': 'GitLab',
                    'Region': aws_region,
                    'GeneratorId': 'gitlab-ci/sast',
                    'AwsAccountId': aws_account_id,
                    'Types': ['Software and Configuration Checks'],
                    'FirstObservedAt': datetime.datetime.now().isoformat(),
                    'LastObservedAt': datetime.datetime.now().isoformat(),
                    'CreatedAt': datetime.datetime.now().isoformat(),
                    'UpdatedAt': datetime.datetime.now().isoformat(),
                    'Severity': {
                        'Label': map_severity(result.get('issue_severity', 'MEDIUM')),
                        'Normalized': map_normalized_severity(result.get('issue_severity', 'MEDIUM'))
                    },
                    'Title': result.get('test_name', 'SAST Finding'),
                    'Description': result.get('issue_text', 'Security issue detected'),
                    'Remediation': {
                        'Recommendation': {
                            'Text': result.get('issue_cwe', {}).get('description', 'Review and fix the security issue'),
                            'Url': 'https://cwe.mitre.org/data/definitions/{}.html'.format(result.get('issue_cwe', {}).get('id', '79'))
                        }
                    },
                    'ProductFields': {
                        'GitLab Project': gitlab_project,
                        'Commit SHA': gitlab_commit_sha,
                        'Branch': gitlab_branch
                    },
                    'Resources': [
                        {
                            'Type': 'AwsCodeBuildProject',
                            'Id': f"arn:aws:codebuild:{aws_region}:{aws_account_id}:project/{gitlab_project}",
                            'Partition': 'aws',
                            'Region': aws_region,
                            'Details': {
                                'Other': {
                                    'File': result.get('filename', 'unknown'),
                                    'Line': str(result.get('line_number', 'unknown'))
                                }
                            }
                        }
                    ],
                    'WorkflowState': 'NEW',
                    'Workflow': {
                        'Status': 'NEW'
                    },
                    'RecordState': 'ACTIVE'
                }
                security_hub_findings.append(finding)
        
        if security_hub_findings:
            # Import findings in batches
            for i in range(0, len(security_hub_findings), 100):
                batch = security_hub_findings[i:i+100]
                securityhub.batch_import_findings(Findings=batch)
                print(f"Imported {len(batch)} SAST findings from {report_file}")
            
    except Exception as e:
        print(f"Error importing SAST findings from {report_file}: {e}")

def import_dast_findings(securityhub, report_file, aws_region, aws_account_id, gitlab_project):
    """Import DAST findings to Security Hub"""
    try:
        with open(report_file, 'r') as f:
            report = json.load(f)
        
        security_hub_findings = []
        
        if 'site' in report and 'alerts' in report['site'][0]:
            for alert in report['site'][0]['alerts']:
                finding = {
                    'SchemaVersion': '2018-10-08',
                    'Id': f"dast-{alert.get('pluginid', 'unknown')}-{datetime.datetime.now().isoformat()}",
                    'ProductArn': f"arn:aws:securityhub:{aws_region}:{aws_account_id}:product/dast/gitlab-dast",
                    'ProductName': 'GitLab DAST',
                    'CompanyName': 'GitLab',
                    'Region': aws_region,
                    'GeneratorId': 'gitlab-ci/dast',
                    'AwsAccountId': aws_account_id,
                    'Types': ['Application Vulnerability'],
                    'FirstObservedAt': datetime.datetime.now().isoformat(),
                    'LastObservedAt': datetime.datetime.now().isoformat(),
                    'CreatedAt': datetime.datetime.now().isoformat(),
                    'UpdatedAt': datetime.datetime.now().isoformat(),
                    'Severity': {
                        'Label': map_severity(alert.get('risk', 'Medium')),
                        'Normalized': map_normalized_severity(alert.get('risk', 'Medium'))
                    },
                    'Title': alert.get('name', 'DAST Finding'),
                    'Description': alert.get('desc', 'Web application vulnerability detected'),
                    'Remediation': {
                        'Recommendation': {
                            'Text': alert.get('solution', 'Review and fix the web application vulnerability'),
                            'Url': alert.get('reference', 'https://owasp.org/')
                        }
                    },
                    'ProductFields': {
                        'GitLab Project': gitlab_project,
                        'Target URL': 'https://terence-webster.com'
                    },
                    'Resources': [
                        {
                            'Type': 'AwsEc2Instance',
                            'Id': f"arn:aws:ec2:{aws_region}:{aws_account_id}:instance/web-app",
                            'Partition': 'aws',
                            'Region': aws_region,
                            'Details': {
                                'Other': {
                                    'URL': 'https://terence-webster.com',
                                    'Plugin ID': alert.get('pluginid', 'unknown')
                                }
                            }
                        }
                    ],
                    'WorkflowState': 'NEW',
                    'Workflow': {
                        'Status': 'NEW'
                    },
                    'RecordState': 'ACTIVE'
                }
                security_hub_findings.append(finding)
        
        if security_hub_findings:
            # Import findings in batches
            for i in range(0, len(security_hub_findings), 100):
                batch = security_hub_findings[i:i+100]
                securityhub.batch_import_findings(Findings=batch)
                print(f"Imported {len(batch)} DAST findings")
            
    except Exception as e:
        print(f"Error importing DAST findings: {e}")

if __name__ == "__main__":
    # AWS configuration
    aws_region = 'us-east-1'
    aws_account_id = boto3.client('sts').get_caller_identity()['Account']
    
    # GitLab CI variables
    gitlab_project = os.environ.get('CI_PROJECT_NAME', 'grc-portfolio')
    gitlab_commit_sha = os.environ.get('CI_COMMIT_SHA', 'unknown')
    gitlab_branch = os.environ.get('CI_COMMIT_REF_NAME', 'main')
    
    # Initialize Security Hub client
    securityhub = boto3.client('securityhub', region_name=aws_region)
    
    print("Starting security findings import...")
    
    # Import SAST findings
    import_sast_findings(securityhub, 'bandit-report.json', aws_region, aws_account_id, gitlab_project, gitlab_commit_sha, gitlab_branch)
    import_sast_findings(securityhub, 'safety-report.json', aws_region, aws_account_id, gitlab_project, gitlab_commit_sha, gitlab_branch)
    import_sast_findings(securityhub, 'semgrep-report.json', aws_region, aws_account_id, gitlab_project, gitlab_commit_sha, gitlab_branch)
    
    # Import DAST findings
    import_dast_findings(securityhub, 'dast-report.json', aws_region, aws_account_id, gitlab_project)
    
    print("Security findings import completed!")
