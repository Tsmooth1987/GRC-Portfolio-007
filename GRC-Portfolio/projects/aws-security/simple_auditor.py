import boto3
import argparse
from datetime import datetime

def check_security_groups(profile='default', region='us-east-1'):
    """Simple security group checker"""
    print(f"\n🔍 Starting security group check - {datetime.now()}")
    print("This will list all security groups in your account")
    
    try:
        # Create a session
        session = boto3.Session(profile_name=profile, region_name=region)
        ec2 = session.client('ec2')
        
        # Get all security groups
        response = ec2.describe_security_groups()
        
        print(f"\nFound {len(response['SecurityGroups'])} security groups:")
        print("=" * 50)
        
        # List security groups
        for group in response['SecurityGroups']:
            print(f"\n🔹 {group['GroupName']} ({group['GroupId']})")
            print(f"   Description: {group['Description']}")
            
            # Check for open ports
            for perm in group.get('IpPermissions', []):
                for ip_range in perm.get('IpRanges', []):
                    if ip_range.get('CidrIp') == '0.0.0.0/0':
                        print(f"   ⚠️  WARNING: Open to the world on port {perm.get('FromPort', 'N/A')}")
        
        print("\n✅ Check complete!")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Make sure your AWS credentials are configured correctly.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple AWS Security Group Auditor')
    parser.add_argument('--profile', default='default', help='AWS profile name')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    args = parser.parse_args()
    
    check_security_groups(args.profile, args.region)
