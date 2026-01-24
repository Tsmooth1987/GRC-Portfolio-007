#!/usr/bin/env python3
"""
EC2 Security Group Auditor

This script audits AWS EC2 security groups for:
- Overly permissive rules
- Unused security groups
- Publicly accessible resources
"""

import boto3
import argparse
import json
import csv
from datetime import datetime
from typing import Dict, List, Any, Optional
from botocore.exceptions import ClientError, NoCredentialsError, NoRegionError

class SecurityGroupAuditor:
    def __init__(self, profile: str = 'default', region: str = 'us-east-1'):
        """Initialize the auditor with AWS credentials and region"""
        try:
            session = boto3.Session(profile_name=profile, region_name=region)
            self.ec2 = session.client('ec2')
            self.ec2_resource = session.resource('ec2')
            self.findings = []
            self.region = region
        except NoCredentialsError:
            raise Exception("AWS credentials not found. Please configure your AWS credentials.")
        except NoRegionError:
            raise Exception("AWS region not specified. Please set a default region.")

    def check_public_access(self, sg: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for public access in security group rules"""
        issues = []
        
        for permission in sg.get('IpPermissions', []):
            for ip_range in permission.get('IpRanges', []):
                if ip_range.get('CidrIp') == '0.0.0.0/0':
                    issues.append({
                        'type': 'public_access',
                        'port': permission.get('FromPort', 'All'),
                        'protocol': permission.get('IpProtocol', 'All'),
                        'cidr': '0.0.0.0/0',
                        'description': ip_range.get('Description', 'No description')
                    })
        
        return issues

    def check_unused_security_groups(self) -> List[Dict[str, Any]]:
        """Find security groups that are not in use"""
        try:
            used_sgs = set()
            all_sgs = set(sg['GroupId'] for sg in self.ec2.describe_security_groups()['SecurityGroups'])
            
            # Get SGs used by instances
            instances = self.ec2.describe_instances()
            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    for sg in instance.get('SecurityGroups', []):
                        used_sgs.add(sg['GroupId'])
            
            # Get SGs used by network interfaces
            interfaces = self.ec2.describe_network_interfaces()
            for interface in interfaces['NetworkInterfaces']:
                for group in interface.get('Groups', []):
                    used_sgs.add(group['GroupId'])
            
            unused_sgs = all_sgs - used_sgs
            return [{'group_id': sg_id, 'type': 'unused_sg'} for sg_id in unused_sgs]
            
        except ClientError as e:
            print(f"Error checking unused security groups: {e}")
            return []

    def audit_security_groups(self, vpc_id: Optional[str] = None) -> None:
        """Audit all security groups in the specified VPC (or all VPCs)"""
        try:
            # Get all security groups
            filters = []
            if vpc_id:
                filters.append({'Name': 'vpc-id', 'Values': [vpc_id]})
                
            response = self.ec2.describe_security_groups(Filters=filters)
            
            # Check each security group
            for sg in response['SecurityGroups']:
                # Check for public access
                public_access_issues = self.check_public_access(sg)
                for issue in public_access_issues:
                    self.findings.append({
                        'severity': self._determine_severity(issue['port']),
                        'group_id': sg['GroupId'],
                        'group_name': sg['GroupName'],
                        'issue_type': issue['type'],
                        'details': issue,
                        'vpc_id': sg.get('VpcId', 'default')
                    })
            
            # Check for unused security groups
            unused_sgs = self.check_unused_security_groups()
            for sg in unused_sgs:
                self.findings.append({
                    'severity': 'low',
                    'group_id': sg['group_id'],
                    'group_name': 'N/A',
                    'issue_type': sg['type'],
                    'details': {'status': 'Not attached to any resource'},
                    'vpc_id': 'N/A'
                })
                    
        except ClientError as e:
            print(f"Error auditing security groups: {e}")

    def _determine_severity(self, port: int) -> str:
        """Determine severity based on port number"""
        critical_ports = [22, 3389, 1433, 3306, 5432, 1521, 27017]  # SSH, RDP, common databases
        if port in critical_ports:
            return 'critical'
        elif 0 < port < 1024:  # Well-known ports
            return 'high'
        else:
            return 'medium'

    def generate_report(self, output_format: str = 'csv', output_file: Optional[str] = None) -> None:
        """Generate audit report in specified format"""
        if not output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f'security_group_audit_{timestamp}.{output_format}'
        
        try:
            if output_format.lower() == 'json':
                with open(output_file, 'w') as f:
                    json.dump(self.findings, f, indent=2)
            else:  # Default to CSV
                if not self.findings:
                    print("No findings to report.")
                    return
                    
                # Flatten the findings for CSV
                csv_data = []
                for finding in self.findings:
                    row = {
                        'severity': finding['severity'],
                        'group_id': finding['group_id'],
                        'group_name': finding['group_name'],
                        'issue_type': finding['issue_type'],
                        'vpc_id': finding['vpc_id']
                    }
                    # Add details to the row
                    if isinstance(finding['details'], dict):
                        row.update({f'detail_{k}': v for k, v in finding['details'].items()})
                    else:
                        row['details'] = str(finding['details'])
                    csv_data.append(row)
                
                # Write to CSV
                with open(output_file, 'w', newline='') as f:
                    if csv_data:
                        writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
                        writer.writeheader()
                        writer.writerows(csv_data)
            
            print(f"Report generated successfully: {output_file}")
            
        except Exception as e:
            print(f"Error generating report: {e}")

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='AWS EC2 Security Group Auditor')
    parser.add_argument('--profile', type=str, default='default',
                      help='AWS profile name (default: default)')
    parser.add_argument('--region', type=str, default='us-east-1',
                      help='AWS region (default: us-east-1)')
    parser.add_argument('--output', type=str, choices=['csv', 'json'], default='csv',
                      help='Output format (default: csv)')
    parser.add_argument('--report', type=str, default=None,
                      help='Output file path (default: security_group_audit_<timestamp>.<format>)')
    parser.add_argument('--vpc-id', type=str, default=None,
                      help='Only check security groups in this VPC')
    parser.add_argument('--severity', type=str, choices=['low', 'medium', 'high', 'critical'],
                      default='low', help='Minimum severity to report (default: low)')
    parser.add_argument('--verbose', action='store_true',
                      help='Show detailed output')
    parser.add_argument('--debug', action='store_true',
                      help='Enable debug mode')
    
    return parser.parse_args()

def main():
    """Main function"""
    args = parse_arguments()
    
    try:
        print(f"Starting security group audit in {args.region}...")
        auditor = SecurityGroupAuditor(profile=args.profile, region=args.region)
        
        # Run the audit
        auditor.audit_security_groups(vpc_id=args.vpc_id)
        
        # Filter findings by severity
        severity_levels = ['low', 'medium', 'high', 'critical']
        min_severity_index = severity_levels.index(args.severity.lower())
        filtered_findings = [
            f for f in auditor.findings
            if severity_levels.index(f['severity']) >= min_severity_index
        ]
        
        # Generate report
        if filtered_findings:
            print(f"Found {len(filtered_findings)} security issues (severity: {args.severity}+)")
            auditor.generate_report(
                output_format=args.output,
                output_file=args.report
            )
        else:
            print("No security issues found with the specified criteria.")
            
    except Exception as e:
        print(f"Error during security group audit: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
