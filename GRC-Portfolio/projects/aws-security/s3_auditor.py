# --- S3 Bucket Security Auditor ---

# This script will audit all S3 buckets in the account for two security settings:
# 1. Versioning status
# 2. Public access block status
# It will then generate a CSV report of the findings.


# --- Step 1: Import Libraries and Set Up ---
import boto3
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('s3_auditor.log'), # Log to a file
        logging.StreamHandler() # Also log to the console
    ]
)

logging.info("S3 Auditor script started.")


# --- Step 2: Fetch Bucket List from AWS ---
s3_client = boto3.client('s3')
audit_results = [] # This list will hold the results for each bucket
buckets = [] # This will hold the bucket list from AWS

try:
    logging.info("Connecting to AWS to get S3 bucket list...")
    response = s3_client.list_buckets()
    buckets = response.get('Buckets', []) # Use .get() for safety
    logging.info(f"Successfully found {len(buckets)} buckets to audit.")
except Exception as e:
    logging.error(f"An error occurred while fetching the bucket list: {e}")


# --- Step 3: Loop Through Buckets and Check Settings ---
if buckets: # Only proceed if we have buckets to check
    logging.info("Starting audit of each bucket...")
    for bucket in buckets:
        bucket_name = bucket['Name']
        logging.info(f"--- Checking bucket: {bucket_name} ---")

        try:
            # 1. Check Versioning Status
            versioning_status = 'NotEnabled' # Default to not enabled
            versioning_response = s3_client.get_bucket_versioning(Bucket=bucket_name)
            status = versioning_response.get('Status')
            if status == 'Enabled':
                versioning_status = 'Enabled'
            elif status == 'Suspended':
                versioning_status = 'Suspended'
            
            logging.info(f"  - Versioning Status: {versioning_status}")

            # 2. Check Public Access Block
            public_access_blocked = False # Default to not blocked
            try:
                # This call will succeed if a block is configured
                s3_client.get_public_access_block(Bucket=bucket_name)
                public_access_blocked = True # If the call doesn't error, a block is in place
            except s3_client.exceptions.ClientError as e:
                # This specific error means no public access block is configured.
                if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
                    public_access_blocked = False
                else:
                    # Re-raise other unexpected errors
                    raise e
            
            logging.info(f"  - Public Access Blocked: {public_access_blocked}")

            # 3. Store the results
            audit_results.append({
                'BucketName': bucket_name,
                'VersioningStatus': versioning_status,
                'PublicAccessBlocked': public_access_blocked
            })

        except Exception as e:
            logging.error(f"Could not audit bucket '{bucket_name}'. Error: {e}")

    logging.info("Finished auditing all buckets.")


# --- Step 4: Create and Save the Report ---
if audit_results:
    logging.info("Creating CSV report from audit findings...")
    try:
        # Create a DataFrame from our list of dictionaries
        df = pd.DataFrame(audit_results)
        # Save the DataFrame to a CSV file. index=False prevents pandas from writing row numbers.
        report_path = 's3_security_report.csv'
        df.to_csv(report_path, index=False)
        logging.info(f"Successfully saved report to {report_path}")
    except Exception as e:
        logging.error(f"Could not save the report. Error: {e}")
else:
    logging.warning("No audit results to save to a report.")


logging.info("S3 Auditor script finished.")
