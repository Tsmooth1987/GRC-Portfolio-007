import boto3
import pandas as pd
import logging
import json
import os

# --- Step 1: Setup Logging and AWS Clients ---
# Standard Lambda logging setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Get the SNS Topic ARN from an environment variable for security and flexibility
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

iam_client = boto3.client('iam')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    """
    This is the main entry point for the AWS Lambda function.
    It scans for customer-managed IAM policies with admin access and sends an SNS alert.
    """
    logger.info("IAM Policy Alerter Lambda started.")

    if not SNS_TOPIC_ARN:
        logger.error("FATAL: SNS_TOPIC_ARN environment variable is not set. Aborting.")
        return

    # --- Step 2: Get and Analyze Policies ---
    audit_findings = []
    try:
        logger.info("Connecting to AWS to get IAM policies...")
        paginator = iam_client.get_paginator('list_policies')
        for page in paginator.paginate(Scope='Local'):
            for policy in page['Policies']:
                policy_name = policy['PolicyName']
                policy_arn = policy['Arn']
                default_version_id = policy['DefaultVersionId']

                # Get the policy document
                policy_version = iam_client.get_policy_version(
                    PolicyArn=policy_arn,
                    VersionId=default_version_id
                )
                policy_document = policy_version['PolicyVersion']['Document']

                # Check for admin access
                statements = policy_document.get('Statement', [])
                if not isinstance(statements, list):
                    statements = [statements] # Ensure statements is always a list

                for stmt in statements:
                    is_admin_policy = (
                        stmt.get('Effect') == 'Allow' and
                        stmt.get('Action') == '*' and
                        stmt.get('Resource') == '*'
                    )
                    if is_admin_policy:
                        finding_details = f"Policy '{policy_name}' ({policy_arn}) grants full Administrator Access."
                        logger.warning(f"FOUND ADMIN POLICY: {finding_details}")
                        
                        audit_findings.append({
                            'PolicyName': policy_name,
                            'PolicyARN': policy_arn,
                            'Finding': "Policy grants full Administrator Access ('Allow', '*', '*')"
                        })

                        # --- Step 3: Send SNS Alert ---
                        logger.info(f"Sending alert to SNS topic: {SNS_TOPIC_ARN}")
                        subject = "GRC Alert: Administrator Access Policy Detected!"
                        message = (
                            "An IAM policy with full administrator privileges has been detected in your AWS account.\n\n"
                            f"Policy Name: {policy_name}\n"
                            f"Policy ARN: {policy_arn}\n\n"
                            "This policy should be reviewed immediately to ensure it is intended and necessary."
                        )
                        sns_client.publish(TopicArn=SNS_TOPIC_ARN, Subject=subject, Message=message)
                        logger.info("Successfully sent alert.")
                        break # Move to the next policy once a finding is reported

    except Exception as e:
        logger.error(f"An unexpected error occurred during the audit: {e}")
        # Optionally, send an error notification

    # --- Step 4: Log Completion ---
    if not audit_findings:
        logger.info("Scan complete. No policies with administrator access found.")
    else:
        logger.info(f"Scan complete. Found and reported {len(audit_findings)} admin policy/policies.")

    return {
        'statusCode': 200,
        'body': json.dumps(f'Scan complete. Found {len(audit_findings)} issue(s).')
    }
